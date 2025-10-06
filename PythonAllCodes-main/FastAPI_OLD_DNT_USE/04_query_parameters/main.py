from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory store for items
items = {}

class Item(BaseModel):
    name: str
    description: str = ""
    price: float = 0.0




@app.get("/search/")
def search_items(q: str = None, limit: int = 10):
    # Filter items by query if provided
    filtered = [
        {"item_id": item_id, **item.dict()}
        for item_id, item in items.items()
        if q is None or q.lower() in item.name.lower()
    ]
    return {"query": q, "limit": limit, "results": filtered[:limit]}

@app.post("/search/")
def create_item(item: Item):
    item_id = max(items.keys(), default=0) + 1
    items[item_id] = item
    return {"created": {"item_id": item_id, **item.dict()}}

@app.put("/search/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"updated": {"item_id": item_id, **item.dict()}}

@app.get("/docs")
def get_docs():
    return {"docs_url": "http://127.0.0.1:8000/docs"}