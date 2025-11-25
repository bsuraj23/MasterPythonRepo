"""
FastAPI Beginner Level Interview Questions
===========================================
Comprehensive guide with theory and practical coding questions
"""

# ============================================================================
# SECTION 1: FastAPI Basics - Theory Questions
# ============================================================================

"""
Q1: What is FastAPI and why is it popular?
-------------------------------------------
Answer:
FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+
based on standard Python type hints.

Key Features:
- Fast: Very high performance, on par with NodeJS and Go
- Fast to code: Increases development speed by 200-300%
- Fewer bugs: Reduces human-induced errors by ~40%
- Intuitive: Great editor support with auto-completion
- Easy: Designed to be easy to use and learn
- Standards-based: Based on OpenAPI and JSON Schema
- Automatic documentation: Interactive API docs (Swagger UI & ReDoc)

Why Popular:
1. Type hints validation using Pydantic
2. Async/await support for concurrent operations
3. Automatic API documentation
4. Built-in data validation
5. Dependency injection system
"""

"""
Q2: What is the difference between FastAPI and Flask?
------------------------------------------------------
FastAPI:
- Modern (2018), built on Starlette and Pydantic
- Async/await support by default
- Automatic data validation
- Auto-generated API documentation
- Type hints required
- Better performance

Flask:
- Older (2010), mature ecosystem
- Sync by default (async added later)
- Manual validation needed
- No built-in documentation
- Optional type hints
- Simpler for small projects

FastAPI is better for:
- APIs with complex validation
- High-performance requirements
- Projects needing async operations
- Modern Python projects

Flask is better for:
- Simple web applications
- Rapid prototyping
- When you need extensive plugins
"""

"""
Q3: What is ASGI and how does it differ from WSGI?
---------------------------------------------------
ASGI (Asynchronous Server Gateway Interface):
- Async-capable
- Supports WebSockets, HTTP/2
- Better for real-time applications
- Used by FastAPI, Starlette, Django 3.0+

WSGI (Web Server Gateway Interface):
- Synchronous only
- Only HTTP/1.1
- Traditional request-response
- Used by Flask, Django (older versions)

FastAPI uses ASGI servers like:
- Uvicorn (recommended)
- Hypercorn
- Daphne
"""

"""
Q4: What is Pydantic and its role in FastAPI?
----------------------------------------------
Pydantic is a data validation library using Python type hints.

Role in FastAPI:
1. Request body validation
2. Response model validation
3. Configuration management
4. Data serialization/deserialization
5. Automatic documentation generation

Benefits:
- Type safety
- Clear error messages
- IDE autocomplete support
- Reduces boilerplate code
"""

"""
Q5: What is dependency injection in FastAPI?
---------------------------------------------
Dependency injection is a design pattern where dependencies are provided
to a function rather than created inside it.

In FastAPI:
- Uses the Depends() function
- Helps with:
  * Database connections
  * Authentication
  * Configuration
  * Reusable logic
  * Testing

Benefits:
- Code reusability
- Better testing
- Cleaner code
- Separation of concerns
"""

# ============================================================================
# SECTION 2: FastAPI Basics - Coding Questions
# ============================================================================

"""
Q6: Create a basic FastAPI application with a hello world endpoint
-------------------------------------------------------------------
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

# To run: uvicorn filename:app --reload


"""
Q7: Create an endpoint that accepts query parameters
-----------------------------------------------------
"""

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, search: Optional[str] = None):
    """
    Query parameters:
    - skip: number of items to skip (default: 0)
    - limit: maximum items to return (default: 10)
    - search: optional search term
    """
    result = {
        "skip": skip,
        "limit": limit,
        "search": search
    }
    return result

# Example URLs:
# /items/
# /items/?skip=5&limit=20
# /items/?search=phone&limit=5


"""
Q8: Create an endpoint with path parameters and validation
-----------------------------------------------------------
"""

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(
    user_id: int = Path(..., title="User ID", ge=1, le=1000)
):
    """
    Path parameter with validation:
    - user_id must be between 1 and 1000
    """
    return {"user_id": user_id, "name": f"User {user_id}"}

@app.get("/products/{product_id}/reviews/{review_id}")
def read_review(
    product_id: int = Path(..., ge=1),
    review_id: int = Path(..., ge=1)
):
    """Multiple path parameters"""
    return {
        "product_id": product_id,
        "review_id": review_id
    }


"""
Q9: Create a POST endpoint with request body using Pydantic
------------------------------------------------------------
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    age: int = Field(..., ge=0, le=150)
    is_active: bool = True
    full_name: Optional[str] = None

@app.post("/users/")
def create_user(user: User):
    """
    Create a new user with validation
    """
    return {
        "message": "User created successfully",
        "user": user.dict()
    }

# Example request body:
# {
#     "username": "john_doe",
#     "email": "john@example.com",
#     "age": 25,
#     "full_name": "John Doe"
# }


"""
Q10: Create endpoints demonstrating all HTTP methods (CRUD)
------------------------------------------------------------
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool = True

# In-memory database
items_db = {}
item_id_counter = 1

# CREATE
@app.post("/items/", status_code=201)
def create_item(item: Item):
    global item_id_counter
    item_id = item_id_counter
    items_db[item_id] = item.dict()
    item_id_counter += 1
    return {"id": item_id, **item.dict()}

# READ - All items
@app.get("/items/")
def read_items():
    return {"items": items_db}

# READ - Single item
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.dict()
    return {"message": "Item updated", "item": items_db[item_id]}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "item": deleted_item}


# ============================================================================
# SECTION 3: Advanced Beginner Topics - Theory
# ============================================================================

"""
Q11: What are response models in FastAPI?
------------------------------------------
Response models define the structure of API responses.

Benefits:
1. Output data validation
2. Automatic documentation
3. Filtering sensitive data
4. Type conversion

Example use cases:
- Hide password fields
- Convert database models to API responses
- Ensure consistent response structure
"""

"""
Q12: What is the purpose of status codes in APIs?
--------------------------------------------------
HTTP status codes indicate the result of an API request.

Common codes:
- 200 OK: Success
- 201 Created: Resource created
- 204 No Content: Success, no response body
- 400 Bad Request: Invalid input
- 401 Unauthorized: Authentication required
- 403 Forbidden: No permission
- 404 Not Found: Resource doesn't exist
- 500 Internal Server Error: Server error

FastAPI allows setting custom status codes for each endpoint.
"""

"""
Q13: What is the difference between Query and Path parameters?
---------------------------------------------------------------
Path Parameters:
- Part of the URL path
- Required by default
- Used for resource identification
- Example: /users/{user_id}

Query Parameters:
- After ? in URL
- Optional by default
- Used for filtering/pagination
- Example: /users?age=25&active=true

Body Parameters:
- In request body
- For complex data
- Used with POST/PUT/PATCH
"""

"""
Q14: What is HTTPException and when to use it?
-----------------------------------------------
HTTPException is FastAPI's way to return HTTP error responses.

When to use:
- Resource not found (404)
- Validation errors (400)
- Unauthorized access (401)
- Permission denied (403)
- Custom error messages

It automatically:
- Sets the status code
- Returns error details
- Updates API documentation
"""

"""
Q15: What are middleware in FastAPI?
-------------------------------------
Middleware is code that runs before/after each request.

Common uses:
- CORS handling
- Request logging
- Authentication
- Request timing
- Error handling
- Request/response modification

FastAPI supports:
- Starlette middleware
- Custom middleware
- Third-party middleware
"""

# ============================================================================
# SECTION 4: Advanced Beginner - Coding Questions
# ============================================================================

"""
Q16: Implement response models with data filtering
---------------------------------------------------
"""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    # Password is excluded from output

class UserInDB(UserIn):
    hashed_password: str

def fake_hash_password(password: str) -> str:
    return f"hashed_{password}"

@app.post("/users/", response_model=UserOut)
def create_user(user: UserIn):
    """
    Password is accepted in input but not returned in response
    """
    hashed_password = fake_hash_password(user.password)
    user_in_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    
    # Return excludes password
    return user_in_db


"""
Q17: Implement error handling with custom messages
---------------------------------------------------
"""

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Simulated database
users = {
    1: {"name": "John", "email": "john@example.com"},
    2: {"name": "Jane", "email": "jane@example.com"}
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
            headers={"X-Error": "User does not exist"}
        )
    return users[user_id]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    if user_id == 1:  # Protect admin user
        raise HTTPException(
            status_code=403,
            detail="Cannot delete admin user"
        )
    deleted_user = users.pop(user_id)
    return {"message": "User deleted", "user": deleted_user}


"""
Q18: Implement query parameters with validation
------------------------------------------------
"""

from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

@app.get("/search/")
def search_items(
    q: str = Query(..., min_length=3, max_length=50, description="Search query"),
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Page size"),
    sort: Optional[str] = Query(None, regex="^(asc|desc)$"),
    tags: List[str] = Query([], description="Filter by tags")
):
    """
    Search endpoint with validated query parameters
    """
    return {
        "query": q,
        "page": page,
        "size": size,
        "sort": sort,
        "tags": tags,
        "results": []
    }

# Example URLs:
# /search/?q=laptop&page=2&size=20&sort=asc&tags=electronics&tags=sale


"""
Q19: Implement dependency injection for database connection
------------------------------------------------------------
"""

from fastapi import FastAPI, Depends
from typing import Generator

app = FastAPI()

# Simulated database connection
class Database:
    def __init__(self):
        self.connection = "Connected to DB"
    
    def get_data(self, table: str):
        return f"Data from {table}"
    
    def close(self):
        self.connection = None

def get_db() -> Generator:
    """
    Dependency that provides database connection
    """
    db = Database()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def read_items(db: Database = Depends(get_db)):
    """
    Endpoint using database dependency
    """
    data = db.get_data("items")
    return {"data": data}

@app.get("/users/")
def read_users(db: Database = Depends(get_db)):
    """
    Another endpoint reusing the same dependency
    """
    data = db.get_data("users")
    return {"data": data}


"""
Q20: Implement background tasks
--------------------------------
"""

from fastapi import FastAPI, BackgroundTasks
from typing import Dict
import time

app = FastAPI()

def write_log(message: str):
    """Background task to write logs"""
    time.sleep(2)  # Simulate slow operation
    with open("log.txt", "a") as f:
        f.write(f"{time.ctime()}: {message}\n")

def send_email(email: str, message: str):
    """Background task to send email"""
    time.sleep(3)  # Simulate email sending
    print(f"Email sent to {email}: {message}")

@app.post("/send-notification/")
def send_notification(
    email: str,
    message: str,
    background_tasks: BackgroundTasks
):
    """
    Send notification and log in background
    Returns immediately without waiting for tasks
    """
    background_tasks.add_task(write_log, f"Notification to {email}")
    background_tasks.add_task(send_email, email, message)
    
    return {"message": "Notification will be sent in background"}


# ============================================================================
# SECTION 5: Database Integration - Theory & Code
# ============================================================================

"""
Q21: What is SQLAlchemy and how does it work with FastAPI?
-----------------------------------------------------------
SQLAlchemy is a Python SQL toolkit and ORM (Object Relational Mapper).

Components:
1. Core: SQL expression language
2. ORM: Object-Relational Mapping

Benefits with FastAPI:
- Type-safe database operations
- Automatic model-to-dict conversion
- Migration support
- Multiple database support (MySQL, PostgreSQL, SQLite)
- Query optimization

Integration pattern:
1. Define database models
2. Create Pydantic schemas
3. Use dependency injection for sessions
4. Implement CRUD operations
"""

"""
Q22: Implement complete CRUD with SQLAlchemy (Simplified version)
------------------------------------------------------------------
"""

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy Model
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

# Pydantic Schemas
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int
    
    class Config:
        from_attributes = True

# FastAPI app
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD endpoints
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserDB(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(UserDB).offset(skip).limit(limit).all()
    return users


# ============================================================================
# SECTION 6: Practice Questions
# ============================================================================

"""
Q23: Create a book management API with the following requirements:
-------------------------------------------------------------------
- Create a book (title, author, price, ISBN)
- Get all books with pagination
- Get book by ISBN
- Update book price
- Delete book
- Search books by author

Include proper validation and error handling.
"""

"""
Q24: Create an API for a todo list application:
------------------------------------------------
- Add todo (title, description, priority)
- List all todos with filtering by priority
- Mark todo as complete
- Update todo
- Delete todo
- Get statistics (total, completed, pending)
"""

"""
Q25: Create a product catalog API:
-----------------------------------
- Add product (name, description, price, category, stock)
- List products with pagination and sorting
- Filter products by category and price range
- Update product stock
- Search products by name
- Get product statistics by category
"""

# ============================================================================
# TIPS FOR INTERVIEW SUCCESS
# ============================================================================

"""
1. KEY CONCEPTS TO MASTER:
   - Path and query parameters
   - Request body with Pydantic
   - Response models
   - Dependency injection
   - Error handling
   - Database integration
   - Background tasks

2. COMMON INTERVIEW PATTERNS:
   - CRUD operations
   - Authentication basics
   - Data validation
   - Error handling
   - Database queries

3. WHAT INTERVIEWERS LOOK FOR:
   - Code organization
   - Proper error handling
   - Data validation
   - Clean code practices
   - Understanding of REST principles

4. HANDS-ON PRACTICE:
   - Build 3-4 small APIs
   - Practice with databases
   - Implement authentication
   - Write API tests
   - Read FastAPI documentation

5. RESOURCES:
   - Official FastAPI docs (fastapi.tiangolo.com)
   - FastAPI GitHub examples
   - Build real projects
   - Practice on LeetCode/HackerRank
"""

if __name__ == "__main__":
    print("FastAPI Beginner Interview Questions")
    print("=" * 50)
    print("Study these questions and practice the code examples")
    print("Run each code block separately to understand the concepts")
