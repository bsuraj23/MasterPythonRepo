# Enforcing data types and handling missing fields
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum

class OrderStatus(str, Enum):
    """Enum for order status - enforces specific values"""
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

class Order(BaseModel):
    """Order model with strict data type enforcement"""
    id: int = Field(..., gt=0, description="Order ID must be positive")
    item: str = Field(..., min_length=1, max_length=100, description="Item name")
    quantity: int = Field(..., gt=0, le=1000, description="Quantity must be 1-1000")
    price: float = Field(..., gt=0, description="Price must be positive")
    status: OrderStatus = OrderStatus.pending
    customer_email: Optional[str] = Field(None, regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    notes: Optional[str] = Field(None, max_length=500)
    
    @validator('item')
    def item_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Item name cannot be empty or just whitespace')
        return v.strip()
    
    @validator('price')
    def reasonable_price(cls, v):
        if v > 100000:
            raise ValueError('Price seems unreasonably high')
        return v

class OrderCreate(BaseModel):
    """Model for creating orders - excludes auto-generated fields"""
    item: str = Field(..., min_length=1, max_length=100)
    quantity: int = Field(..., gt=0, le=1000)
    price: float = Field(..., gt=0)
    customer_email: Optional[str] = Field(None, regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    notes: Optional[str] = Field(None, max_length=500)

class OrderUpdate(BaseModel):
    """Model for updating orders - all fields optional"""
    item: Optional[str] = Field(None, min_length=1, max_length=100)
    quantity: Optional[int] = Field(None, gt=0, le=1000)
    price: Optional[float] = Field(None, gt=0)
    status: Optional[OrderStatus] = None
    customer_email: Optional[str] = Field(None, regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    notes: Optional[str] = Field(None, max_length=500)

app = FastAPI(
    title="Data Type Enforcement Demo",
    description="Demonstrates strict data validation and type enforcement"
)

# In-memory storage for demo
orders: List[Order] = []
next_id = 1

@app.post("/orders/", response_model=Order)
def create_order(order_data: OrderCreate):
    """Create a new order with automatic ID assignment"""
    global next_id
    
    # Create order with auto-generated ID
    order = Order(
        id=next_id,
        item=order_data.item,
        quantity=order_data.quantity,
        price=order_data.price,
        customer_email=order_data.customer_email,
        notes=order_data.notes
    )
    
    orders.append(order)
    next_id += 1
    return order

@app.get("/orders/", response_model=List[Order])
def get_orders(
    status: Optional[OrderStatus] = Query(None, description="Filter by status"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price filter"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price filter")
):
    """Get all orders with optional filtering"""
    filtered_orders = orders
    
    if status:
        filtered_orders = [o for o in filtered_orders if o.status == status]
    
    if min_price is not None:
        filtered_orders = [o for o in filtered_orders if o.price >= min_price]
        
    if max_price is not None:
        filtered_orders = [o for o in filtered_orders if o.price <= max_price]
    
    return filtered_orders

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int = Field(..., gt=0)):
    """Get a specific order by ID"""
    for order in orders:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, order_update: OrderUpdate):
    """Update an existing order"""
    for i, order in enumerate(orders):
        if order.id == order_id:
            # Update only provided fields
            update_data = order_update.dict(exclude_unset=True)
            updated_order = order.copy(update=update_data)
            orders[i] = updated_order
            return updated_order
    
    raise HTTPException(status_code=404, detail="Order not found")

@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    """Delete an order"""
    for i, order in enumerate(orders):
        if order.id == order_id:
            del orders[i]
            return {"message": f"Order {order_id} deleted successfully"}
    
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/")
def root():
    return {
        "message": "Data Type Enforcement Demo",
        "features": [
            "Strict field validation with Field() constraints",
            "Custom validators for business logic",
            "Enum enforcement for status values",
            "Email validation with regex",
            "Optional field handling",
            "Query parameter validation"
        ],
        "try_invalid_data": {
            "negative_quantity": "POST /orders/ with quantity: -1",
            "invalid_email": "POST /orders/ with customer_email: 'not-an-email'",
            "too_long_item": "POST /orders/ with item name > 100 characters"
        }
    }

# Homework completed: Added GET and PUT endpoints with comprehensive validation
# Additional features: DELETE endpoint, filtering, custom validators, enum usage 
