"""
FastAPI PostgreSQL/MySQL Integration

This module demonstrates comprehensive database integration patterns with FastAPI,
including proper connection management, error handling, and production-ready practices.
"""

from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime
import os
import logging
from contextlib import contextmanager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration with environment variable support
def get_database_url() -> str:
    """
    Get database URL from environment variables or use default SQLite for development
    """
    # Try to get from environment variables first
    db_url = os.getenv("DATABASE_URL")
    
    if db_url:
        return db_url
    
    # Development fallback - use SQLite if no database URL provided
    db_type = os.getenv("DB_TYPE", "sqlite").lower()
    
    if db_type == "postgresql":
        user = os.getenv("DB_USER", "postgres")
        password = os.getenv("DB_PASSWORD", "password")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "5432")
        database = os.getenv("DB_NAME", "testdb")
        return f"postgresql://{user}:{password}@{host}:{port}/{database}"
    
    elif db_type == "mysql":
        user = os.getenv("DB_USER", "root")
        password = os.getenv("DB_PASSWORD", "password")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "3306")
        database = os.getenv("DB_NAME", "testdb")
        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    
    else:
        # SQLite fallback for development
        return "sqlite:///./test_database.db"

# Database setup
DATABASE_URL = get_database_url()
logger.info(f"Using database: {DATABASE_URL.split('://', 1)[0]}://...")

# Create engine with proper configuration
if DATABASE_URL.startswith("sqlite"):
    engine: Engine = create_engine(
        DATABASE_URL, 
        connect_args={"check_same_thread": False},  # SQLite specific
        echo=False  # Set to True for SQL query logging
    )
else:
    engine: Engine = create_engine(
        DATABASE_URL,
        pool_size=5,  # Connection pool size
        max_overflow=10,  # Additional connections beyond pool_size
        pool_pre_ping=True,  # Verify connections before use
        pool_recycle=3600,  # Recycle connections every hour
        echo=False  # Set to True for SQL query logging
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class Item(Base):
    """
    Item model representing items in the database
    """
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    price = Column(String(20), nullable=True)  # Using String to avoid decimal issues
    category = Column(String(50), nullable=True, index=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

# Create tables
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")
except Exception as e:
    logger.error(f"Error creating database tables: {e}")
    raise

# Pydantic Models
class ItemBase(BaseModel):
    """Base item model with common fields"""
    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    description: Optional[str] = Field(None, max_length=1000, description="Item description")
    price: Optional[str] = Field(None, pattern=r"^\d+(\.\d{1,2})?$", description="Item price (e.g., '19.99')")
    category: Optional[str] = Field(None, max_length=50, description="Item category")
    is_active: bool = Field(True, description="Whether the item is active")

class ItemCreate(ItemBase):
    """Model for creating new items"""
    pass

class ItemUpdate(BaseModel):
    """Model for updating existing items (all fields optional)"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    price: Optional[str] = Field(None, pattern=r"^\d+(\.\d{1,2})?$")
    category: Optional[str] = Field(None, max_length=50)
    is_active: Optional[bool] = None

class ItemResponse(ItemBase):
    """Model for item responses"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
    updated_at: datetime

class ItemsListResponse(BaseModel):
    """Model for paginated item list responses"""
    items: List[ItemResponse]
    total: int
    page: int
    per_page: int
    total_pages: int

# FastAPI app
app = FastAPI(
    title="FastAPI Database Integration",
    description="Comprehensive PostgreSQL/MySQL/SQLite integration with FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Database dependency
def get_db():
    """
    Database session dependency with proper error handling
    """
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Database operation failed")
    finally:
        db.close()

# Context manager for database transactions
@contextmanager
def get_db_transaction():
    """
    Context manager for database transactions with automatic rollback on error
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError as e:
        logger.error(f"Transaction failed: {e}")
        db.rollback()
        raise
    finally:
        db.close()

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint to verify database connectivity
    """
    try:
        # Test database connection
        db.execute("SELECT 1")
        return {
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail="Database connection failed")

# CRUD Operations

@app.post("/items/", response_model=ItemResponse, status_code=201, tags=["Items"])
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item
    """
    try:
        # Check if item with same name exists
        existing_item = db.query(Item).filter(Item.name == item.name).first()
        if existing_item:
            raise HTTPException(
                status_code=400, 
                detail=f"Item with name '{item.name}' already exists"
            )
        
        # Create new item
        db_item = Item(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        logger.info(f"Created item: {db_item.name} (ID: {db_item.id})")
        return db_item
        
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Integrity error creating item: {e}")
        raise HTTPException(status_code=400, detail="Data integrity constraint violation")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error creating item: {e}")
        raise HTTPException(status_code=500, detail="Failed to create item")

@app.get("/items/", response_model=ItemsListResponse, tags=["Items"])
def read_items(
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(10, ge=1, le=100, description="Items per page"),
    category: Optional[str] = Query(None, description="Filter by category"),
    active_only: bool = Query(True, description="Show only active items"),
    search: Optional[str] = Query(None, description="Search in name and description"),
    db: Session = Depends(get_db)
):
    """
    Get all items with pagination, filtering, and search
    """
    try:
        # Build query
        query = db.query(Item)
        
        # Apply filters
        if active_only:
            query = query.filter(Item.is_active == True)
        
        if category:
            query = query.filter(Item.category == category)
        
        if search:
            search_term = f"%{search}%"
            query = query.filter(
                (Item.name.like(search_term)) | 
                (Item.description.like(search_term))
            )
        
        # Get total count
        total = query.count()
        
        # Apply pagination
        offset = (page - 1) * per_page
        items = query.order_by(Item.created_at.desc()).offset(offset).limit(per_page).all()
        
        # Calculate total pages
        total_pages = (total + per_page - 1) // per_page
        
        return ItemsListResponse(
            items=items,
            total=total,
            page=page,
            per_page=per_page,
            total_pages=total_pages
        )
        
    except SQLAlchemyError as e:
        logger.error(f"Database error reading items: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve items")

@app.get("/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get a specific item by ID
    """
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item
    except SQLAlchemyError as e:
        logger.error(f"Database error reading item {item_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve item")

@app.put("/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def update_item(item_id: int, item_update: ItemUpdate, db: Session = Depends(get_db)):
    """
    Update an existing item
    """
    try:
        # Check if item exists
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        # Update only provided fields
        update_data = item_update.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")
        
        # Check for name conflicts (if name is being updated)
        if "name" in update_data:
            existing_item = db.query(Item).filter(
                Item.name == update_data["name"],
                Item.id != item_id
            ).first()
            if existing_item:
                raise HTTPException(
                    status_code=400,
                    detail=f"Item with name '{update_data['name']}' already exists"
                )
        
        # Apply updates
        for field, value in update_data.items():
            setattr(db_item, field, value)
        
        db_item.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_item)
        
        logger.info(f"Updated item: {db_item.name} (ID: {db_item.id})")
        return db_item
        
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Integrity error updating item {item_id}: {e}")
        raise HTTPException(status_code=400, detail="Data integrity constraint violation")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error updating item {item_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to update item")

@app.delete("/items/{item_id}", tags=["Items"])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item (soft delete by setting is_active to False)
    """
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        # Soft delete - just mark as inactive
        db_item.is_active = False
        db_item.updated_at = datetime.utcnow()
        db.commit()
        
        logger.info(f"Soft deleted item: {db_item.name} (ID: {db_item.id})")
        return {"message": "Item deleted successfully"}
        
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error deleting item {item_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete item")

@app.delete("/items/{item_id}/permanent", tags=["Items"])
def delete_item_permanent(item_id: int, db: Session = Depends(get_db)):
    """
    Permanently delete an item from the database
    """
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        item_name = db_item.name
        db.delete(db_item)
        db.commit()
        
        logger.info(f"Permanently deleted item: {item_name} (ID: {item_id})")
        return {"message": "Item permanently deleted"}
        
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error permanently deleting item {item_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to permanently delete item")

# Utility endpoints

@app.get("/categories/", tags=["Categories"])
def get_categories(db: Session = Depends(get_db)):
    """
    Get all unique categories
    """
    try:
        categories = db.query(Item.category).filter(
            Item.category.isnot(None),
            Item.is_active == True
        ).distinct().all()
        
        return {
            "categories": [cat[0] for cat in categories if cat[0]]
        }
    except SQLAlchemyError as e:
        logger.error(f"Database error getting categories: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve categories")

@app.get("/stats/", tags=["Statistics"])
def get_statistics(db: Session = Depends(get_db)):
    """
    Get database statistics
    """
    try:
        total_items = db.query(Item).count()
        active_items = db.query(Item).filter(Item.is_active == True).count()
        inactive_items = total_items - active_items
        
        categories_count = db.query(Item.category).filter(
            Item.category.isnot(None),
            Item.is_active == True
        ).distinct().count()
        
        return {
            "total_items": total_items,
            "active_items": active_items,
            "inactive_items": inactive_items,
            "categories_count": categories_count,
            "database_type": DATABASE_URL.split("://", 1)[0]
        }
    except SQLAlchemyError as e:
        logger.error(f"Database error getting statistics: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve statistics")

@app.get("/", tags=["Documentation"])
def root():
    """
    API documentation and information
    """
    return {
        "title": "FastAPI Database Integration",
        "description": "Comprehensive PostgreSQL/MySQL/SQLite integration example",
        "version": "1.0.0",
        "features": [
            "Complete CRUD operations",
            "Pagination and filtering",
            "Search functionality",
            "Soft delete support",
            "Connection pooling",
            "Error handling",
            "Health checks",
            "Statistics endpoint"
        ],
        "database_support": ["PostgreSQL", "MySQL", "SQLite"],
        "endpoints": {
            "docs": "/docs",
            "redoc": "/redoc",
            "health": "/health",
            "items": "/items/",
            "stats": "/stats/",
            "categories": "/categories/"
        }
    }