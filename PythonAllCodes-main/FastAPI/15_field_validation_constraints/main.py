# Field validation and constraints (min_length, max_length, regex)
from fastapi import FastAPI
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    code: str = Field(..., pattern=r"^[A-Z]{3} AA \d{3}$")

app = FastAPI()

@app.post("/products/")
def create_product(product: Product):
    return product
