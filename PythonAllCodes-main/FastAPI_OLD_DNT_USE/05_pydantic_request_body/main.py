
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
    origin: str

# In-memory store for items
items_db = {}


class Student(BaseModel):
    name: str
    age: int
    grade: str

@app.get("/students/")
def get_all_students():
    return [{"name": "Dheeraj23", "age": 20, "grade": "A++"}, {"name": "Sashi", "age": 22, "grade": "B++"}]   





@app.get("/items/")
def get_all_items():
    return list(items_db.values())

@app.post("/items/")
def create_item(item: Item):
    items_db[item.name] = item
    return item

@app.get("/items/{name}")
def get_item(name: str):
    result = items_db.get(name)
    if result:
        return result
    return {"error": "Item not found check very keenly"}

@app.put("/items/{name}")
def update_item(name: str, item: Item):
    items_db[name] = item
    return item
