from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    
class Student(BaseModel):
    name:str
    id:int

class ResponseModel(BaseModel):
    items: List[Item]
    count: int

@app.get("/coolies/", response_model=ResponseModel)
def functionName():
    items = [Student(name="Vinay", id=12)]
    return {"Student": Student, "count": len(Student)}

@app.get("/items/", response_model=ResponseModel)
def get_items():
    items = [Item(name="item1", price=10.0), 
             Item(name="item2", price=20.0),
             Item(name="item3", price=34.0)]
    return {"items": items, "count": len(items)}

@app.get("/getZero",response_model=ResponseModel)
def functionName():
   return {"items": items, "count": len(items)}