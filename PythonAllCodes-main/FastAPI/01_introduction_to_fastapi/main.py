from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Introduction",
    description="A simple FastAPI application demonstrating basic concepts",
    version="1.0.0"
)

# In-memory store for items
items = {}

# Pydantic model for item creation
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None

# Basic root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!", "docs": "/docs", "redoc": "/redoc"}

# Get all items
@app.get("/items/")
def read_items():
    return {"items": items}

# Get item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": items[item_id]}

# Create a new item
@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item.dict()
    return {"item_id": item_id, "item": items[item_id]}

# Simple health check
@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "FastAPI is running!"}
