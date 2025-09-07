from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

items: Dict[int, Item] = {}

@app.get("/items", response_model=Dict[int, Item], tags=["Items"])
def get_items(min_price: Optional[float] = Query(None, ge=0)):
    if min_price is not None:
        return {i: item for i, item in items.items() if item.price >= min_price}
    return items

@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: int):
    if item_id in items:
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Dict[str, int], status_code=201, tags=["Items"])
def create_item(item: Item):
    item_id = max(items.keys(), default=0) + 1
    items[item_id] = item
    return {"item_id": item_id}

@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

@app.delete("/items/{item_id}", response_model=Dict[str, int], tags=["Items"])
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"deleted": item_id}
    raise HTTPException(status_code=404, detail="Item not found")