# Enforcing data types and handling missing fields
from fastapi import FastAPI
from pydantic import BaseModel

class Order(BaseModel):
    id: int
    item: str
    quantity: int

app = FastAPI()

@app.post("/orders/")
def create_order(order: Order):
    return order
