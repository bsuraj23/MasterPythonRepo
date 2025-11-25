from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from pydantic import BaseModel, EmailStr, validator
from typing import List

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Create tables
Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        orm_mode = True

app = FastAPI(
    title="Database Integration Example",
    description="Demonstrates proper database integration with error handling"
)

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user with proper error handling"""
    try:
        db_user = User(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail=f"User with email {user.email} already exists"
        )
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500, 
            detail="Database error occurred while creating user"
        )

@app.get("/users/", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all users with pagination"""
    try:
        users = db.query(User).offset(skip).limit(limit).all()
        return users
    except SQLAlchemyError:
        raise HTTPException(
            status_code=500, 
            detail="Database error occurred while fetching users"
        )

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """Get a specific user by ID"""
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except SQLAlchemyError:
        raise HTTPException(
            status_code=500, 
            detail="Database error occurred while fetching user"
        )

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db)):
    """Update an existing user"""
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        db_user.name = user_update.name
        db_user.email = user_update.email
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail=f"User with email {user_update.email} already exists"
        )
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500, 
            detail="Database error occurred while updating user"
        )

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user"""
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        db.delete(db_user)
        db.commit()
        return {"message": f"User {user_id} deleted successfully"}
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500, 
            detail="Database error occurred while deleting user"
        )

@app.get("/")
def root():
    return {
        "message": "Database Integration with Error Handling",
        "features": [
            "Proper session management with dependency injection",
            "Comprehensive error handling for database operations",
            "Email validation and duplicate prevention",
            "Complete CRUD operations",
            "Proper response models with ORM mode"
        ]
    }

# Homework completed: Added comprehensive error handling for duplicate emails and database connection issues
# Additional features: Proper session management, validation, complete CRUD operations