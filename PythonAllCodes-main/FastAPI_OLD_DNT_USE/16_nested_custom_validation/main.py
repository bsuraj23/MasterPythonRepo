# Nested models and custom validation
from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import List

class Address(BaseModel):
    city: str
    zip_code: str

class Customer(BaseModel):
    name: str
    addresses: List[Address]

    @validator('addresses')
    def check_addresses(cls, v):
        if not v:
            raise ValueError('At least one address required')
        return v

app = FastAPI()

@app.post("/customers/")
def create_customer(customer: Customer):
    return customer
