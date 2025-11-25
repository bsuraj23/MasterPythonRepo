# Data serialization and response customization
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Person(BaseModel):
    """Complete person model with all fields"""
    name: str = Field(..., min_length=1, max_length=100)
    building: str
    ice_cream_flavor: str
    phone: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        # Example of serialization customization
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class PersonResponse(BaseModel):
    """Response model - excludes sensitive data"""
    name: str
    building: str
    ice_cream_flavor: str
    # Note: phone and created_at are excluded for privacy

class PersonWithoutPhone(BaseModel):
    """Simplified person model without phone"""
    name: str = Field(..., min_length=1)
    building: str
    ice_cream_flavor: str

app = FastAPI(
    title="Data Serialization Demo",
    description="Demonstrates response models and data customization"
)

# Sample data
sample_persons = [
    Person(name="John Doe", building="Building A", ice_cream_flavor="Vanilla", phone="123-456-7890"),
    Person(name="Jane Smith", building="Building B", ice_cream_flavor="Chocolate", phone="987-654-3210"),
    Person(name="Alice Brown", building="Building C", ice_cream_flavor="Strawberry")  # No phone
]

@app.get("/persons/", response_model=List[PersonResponse])
def get_persons():
    """Returns persons without sensitive data (phone, created_at)"""
    return sample_persons

@app.get("/persons/full/", response_model=List[Person])
def get_persons_full():
    """Returns complete person data including sensitive fields"""
    return sample_persons

@app.get("/persons/{person_id}", response_model=PersonResponse)
def get_person(person_id: int):
    """Get a specific person by ID"""
    if person_id < 0 or person_id >= len(sample_persons):
        return {"error": "Person not found"}
    return sample_persons[person_id]

@app.post("/persons/", response_model=PersonResponse)
def create_person(person: Person):
    """Create new person and return sanitized response"""
    sample_persons.append(person)
    return person  # FastAPI automatically uses response_model to filter

@app.get("/")
def root():
    return {
        "message": "Data Serialization and Response Customization Demo",
        "endpoints": {
            "get_all_persons": "/persons/ (filtered response)",
            "get_full_persons": "/persons/full/ (complete data)",
            "get_person": "/persons/{id}",
            "create_person": "POST /persons/"
        },
        "note": "Compare /persons/ vs /persons/full/ to see response filtering"
    }

# Homework: Add custom serialization for different user roles (admin sees all data, user sees limited data)
