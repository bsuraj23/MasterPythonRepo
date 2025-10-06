# Data serialization and response customization
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    price: float

app = FastAPI()

@app.get("/items/", response_model=List[Item])
def get_items():
    items = [Item(name="item1", price=10.0), Item(name="item2", price=20.0)]
    return items
