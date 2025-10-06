from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, Dict

#TODO 
# global exception like java where on wrong data pydantic for price shows price error
# class PriceError(HTTPException):
#     def __init__(self, detail: str = "Own msg --Price must be a positive number"):
#         super().__init__(status_code=400, detail=detail)
# class DescriptionError(HTTPException):
#     def __init__(self, detail: str = "Own msg -- Description must be a string"):
#         super().__init__(status_code=400, detail=detail)
# class NameError(HTTPException):
#     def __init__(self, detail: str = "Own msg -- Name must be a string"):
#         super().__init__(status_code=400, detail=detail)


app = FastAPI()

class Item():
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
    # raise PriceError() if item.price <= 0 else {"item_id": item_id}
    # #raise for global exception description and name
    # raise DescriptionError() if item.description is None else {"item_id": item_id}
    # raise NameError() if item.name is None else {"item_id": item_id}
    # #code for description error and name error when other datatype than string is passed
    # raise PriceError() if item.price <= 0 else {"item_id": item_id}
    # # raise DescriptionError() if item.description is not ""  else {"item_id": item_id}
    # raise NameError() if item.name is None else {"item_id": item_id}
    # #code for description error and name error when other datatype than string is passed
    # raise DescriptionError() if not isinstance(item.description, str) else {"item_id": item_id}
    # raise NameError() if not isinstance(item.name, str) else {"item_id": item_id}
    

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



