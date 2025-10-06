
from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory store for items
items = {} # Dictionary to hold items with integer keys

@app.get("/items")  #decorator
def get_items():
    return items

@app.post("/items")
def create_item(item_id: int,item: dict):
    # Add item with next available integer key
    item_id = max(items.keys(), default=0) + 1
    items[item_id] = item
    return {"created": {"item_id": item_id, "item": item}}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    if item_id not in items:
        # If not present, add as new
        items[item_id] = item
        return {"added": {"item_id": item_id, "item": item}}
    items[item_id] = item
    return {"updated": {"item_id": item_id, "item": item}}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"deleted": item_id}
    raise HTTPException(status_code=404, detail="Item not found .....")
