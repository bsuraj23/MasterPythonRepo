from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str


class XYZ(BaseModel):
    
        x: str
        y: int 
        b: float
        message: str
        z: bool
    

@app.get("/wednesday/HelloWorld", response_model=XYZ)
def function():
    return {"message": "Hello, World!", "x": "989898", "y": 123, "b": 45.67, "z": True}



  

class ResponseModel(BaseModel):
    items: List[Item]
    count: int
    addreess: str 

@app.get("/hello", response_model=ResponseModel)
def function():
    return {"items": [{"name": "Hello, World!"}], "count": 1, "addreess": "123 Main St"}



    



@app.get("/hellowithoutresponseModel")
def function():
    return 1110


class Other(BaseModel):
    number: int
    address: str


@app.post("/postAPI1/")
def create_item23(OtherObj: Other):
    item_id = max(items.keys(), default=0) + 1
    items[item_id] = OtherObj
    return {"created": {"item_id": item_id, **OtherObj.dict()}}




# @app.get("/coolies/", response_model=ResponseModel)
# def functionName23():
#     items = [Student(name="Vinay", id=12)]
#     return {"Student": Student, "count": len(Student)}



class ResponseModel2(BaseModel):
    
    count: int

@app.get("/items/", response_model=ResponseModel2)
def get_items():
    items = [Item(name="item1", price=10.0), 
             Item(name="item2", price=20.0),
             Item(name="item3", price=34.0)]
    return {"count": len(items)}

@app.get("/getZero",response_model=ResponseModel)
def functionName():
     items = [Item(name="item1", price=10.0), 
             Item(name="item2", price=20.0),
             ]
     return {"items": items, "count": len(items)}


#Homework   add put and post and try to use the response model 