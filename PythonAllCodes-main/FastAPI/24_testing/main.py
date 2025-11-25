
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

# Main application
app=  FastAPI(title="Testing Demo API")



# Models
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    in_stock: bool = True

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None
    in_stock: bool = True

# In-memory database for demo
items_db: List[ItemResponse] = []
next_id = 1

# Dependency for database session (can be overridden in tests)
def get_database():
    return items_db


def add(a,b):
    return a+b


def sqrt(x):
    """Returns the square root of x"""
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return x ** 0.5


    

# Routes
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI testing!", "version": "1.0.0"}



@app.get("/items/", response_model=List[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: List = Depends(get_database)):
    return db[skip: skip + limit]



@app.post("/items/xyz/rtrtr", response_model=ItemResponse)
def create_item(item: Item, db: List = Depends(get_database)):
    global next_id
    item_with_id = ItemResponse(id=next_id, **item.dict())
    db.append(item_with_id)
    next_id += 1
    return item_with_id


@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: List = Depends(get_database)):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: Item, db: List = Depends(get_database)):
    for i, existing_item in enumerate(db):
        if existing_item.id == item_id:
            updated_item = ItemResponse(id=item_id, **item.dict())
            db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: List = Depends(get_database)):
    for i, item in enumerate(db):
        if item.id == item_id:
            del db[i]
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# Route that can cause errors (for testing error handling)
@app.get("/items/{item_id}")
def get_expensive_item(item_id: int, db: List = Depends(get_database)):
    """Returns item only if it's expensive (price > 100)"""
    for item in db:
        if item.id == item_id:
            if item.price <= 100:
                raise HTTPException(
                    status_code=400, 
                    detail="Item is not expensive enough"
                )
            return item
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Homework: Write comprehensive tests for this API using pytest and TestClient
# Test file should be created as test_main.py in the same directory