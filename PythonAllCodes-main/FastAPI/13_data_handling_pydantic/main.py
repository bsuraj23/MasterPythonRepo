# Data Handling with Pydantic
# Pydantic is used in FastAPI for data validation and parsing using Python type hints.
# It ensures that incoming data matches the expected types and constraints.

from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
    created_at: datetime = datetime.now()
    
    @validator('age')
    def validate_age(cls, v):
        if v < 0 or v > 150:
            raise ValueError('Age must be between 0 and 150')
        return v

@app.post("/users/")
def create_user(user: User):
    """Create a user with Pydantic validation"""
    return {"message": "User created", "user": user}

@app.get("/")
def root():
    return {"message": "Pydantic data validation example", "docs": "/docs"} 