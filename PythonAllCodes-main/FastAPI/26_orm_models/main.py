from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import List, Optional

#DATABASE_URL = "sqlite:///./orm_demo.db"
DATABASE_URL="mysql+pymysql://user:password@localhost/dbname"


enginewewe = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=enginewewe, autoflush=False, autocommit=False)
Base = declarative_base()



# Create tables in the database
Base.metadata.create_all(bind=engine)

# Pydantic models for API
class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    in_stock: bool = True
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Product name cannot be empty')
        return v.strip()

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    in_stock: Optional[bool] = None

class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

# ORM Model definitions
class Product(Base):
    """Product ORM model with comprehensive fields"""
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



@app.get("/products/", response_model=List[ProductResponse])
def read_products(
    skip: int = 0, 
    limit: int = 100, 
    in_stock: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    """Get all products with optional filtering"""
    query = db.query(Product)
    
    if in_stock is not None:
        query = query.filter(Product.in_stock == in_stock)
    
    products = query.offset(skip).limit(limit).all()
    return products

class CategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    
    class Config:
        orm_mode = True

app = FastAPI(
    title="ORM Models and CRUD Operations Demo",
    description="Comprehensive example of SQLAlchemy ORM models with full CRUD operations"
)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Category(Base):
    """Category ORM model"""
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    categoryxyz = Column(String, nullable=True)


@app.get("/categories/", response_model=List[CategoryResponse])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all categories"""
    categories = db.query(Category).offset(skip).limit(limit).all()
    return categories


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = Field(None, max_length=200)


# Category CRUD endpoints
@app.post("/categories/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """Create a new category"""
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# Product CRUD endpoints

@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Create a new product"""
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

#delete endpoint for product 
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a product"""
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    
    return {"message": f"Product {product_id} deleted successfully"}



@app.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """Get a specific product by ID"""
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, 
    product_update: ProductUpdate, 
    db: Session = Depends(get_db)
):
    """Update an existing product"""
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Update only provided fields
    update_data = product_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)
    
    db_product.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a product"""
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": f"Product {product_id} deleted successfully"}



@app.get("/categories/", response_model=List[CategoryResponse])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all categories"""
    categories = db.query(Category).offset(skip).limit(limit).all()
    return categories

# Search and filter endpoints
@app.get("/products/search/", response_model=List[ProductResponse])
def search_products(
    q: str = "",
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    db: Session = Depends(get_db)
):
    """Search products by name and filter by price"""
    query = db.query(Product)
    
    if q:
        query = query.filter(Product.name.contains(q))
    
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    
    return query.all()

@app.get("/")
def root():
    return {
        "message": "ORM Models and CRUD Operations Demo",
        "features": [
            "Complete Product and Category models",
            "Full CRUD operations for both entities",
            "Advanced filtering and search",
            "Proper field validation",
            "Timestamps and audit fields",
            "Response models with ORM mode"
        ],
        "endpoints": {
            "products": "/products/",
            "categories": "/categories/",
            "search": "/products/search/?q=name&min_price=10&max_price=100"
        }
    }

# Homework completed: Implemented comprehensive CRUD operations for Product model
# Additional features: Category model, search functionality, filtering, proper validation