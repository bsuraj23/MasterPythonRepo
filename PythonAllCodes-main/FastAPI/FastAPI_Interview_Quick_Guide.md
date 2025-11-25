# FastAPI Beginner Interview Guide

## Quick Reference for Interview Preparation

### 📚 Theory Questions (Must Know)

#### 1. **What is FastAPI?**
- Modern Python web framework for building APIs
- Based on standard Python type hints
- High performance (on par with NodeJS and Go)
- Auto-generates interactive API documentation

#### 2. **FastAPI vs Flask**
| Feature | FastAPI | Flask |
|---------|---------|-------|
| Performance | Very Fast | Moderate |
| Async Support | Built-in | Added later |
| Data Validation | Automatic | Manual |
| Documentation | Auto-generated | Manual |
| Type Hints | Required | Optional |

#### 3. **Key Components**
- **ASGI**: Async server interface (vs WSGI for Flask)
- **Pydantic**: Data validation using type hints
- **Uvicorn**: ASGI server to run the app
- **Starlette**: Web microframework (FastAPI is built on it)

#### 4. **HTTP Methods**
```
GET     - Retrieve data
POST    - Create new resource
PUT     - Update entire resource
PATCH   - Partial update
DELETE  - Remove resource
```

#### 5. **Status Codes**
```
200 - OK
201 - Created
204 - No Content
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
500 - Server Error
```

---

## 💻 Code Patterns (Most Common)

### Pattern 1: Basic App Setup
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

### Pattern 2: Path Parameters
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### Pattern 3: Query Parameters
```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### Pattern 4: Request Body (POST)
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
```

### Pattern 5: Response Model
```python
class UserOut(BaseModel):
    username: str
    email: str
    # Password excluded from response

@app.post("/users/", response_model=UserOut)
def create_user(user: UserIn):
    return user
```

### Pattern 6: Error Handling
```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
```

### Pattern 7: Dependency Injection
```python
from fastapi import Depends

def get_db():
    db = Database()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def read_items(db = Depends(get_db)):
    return db.get_items()
```

### Pattern 8: Database CRUD
```python
from sqlalchemy.orm import Session

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

---

## 🎯 Common Interview Questions

### Q1: Create a simple TODO API
**Requirements:**
- Add todo
- List all todos
- Mark as complete
- Delete todo

### Q2: Implement user registration
**Requirements:**
- Validate email format
- Password length check
- Return user without password
- Handle duplicate emails

### Q3: Build product search API
**Requirements:**
- Search by name
- Filter by price range
- Pagination support
- Sort by price

### Q4: Create authentication endpoint
**Requirements:**
- Login with username/password
- Return token on success
- Handle invalid credentials

### Q5: Implement CRUD with database
**Requirements:**
- SQLAlchemy integration
- Proper error handling
- Input validation
- Response models

---

## 🔥 Top Tips for Success

### Before Interview:
1. ✅ Practice basic CRUD operations
2. ✅ Understand Pydantic validation
3. ✅ Know dependency injection
4. ✅ Practice error handling
5. ✅ Review HTTP methods and status codes

### During Interview:
1. 📝 Ask clarifying questions
2. 🎯 Start with simple solution, then improve
3. 💬 Explain your thought process
4. 🐛 Test edge cases
5. 📚 Mention FastAPI features (auto docs, validation)

### Common Mistakes to Avoid:
- ❌ Forgetting type hints
- ❌ Not handling errors
- ❌ Ignoring validation
- ❌ Hardcoding values
- ❌ No response models

---

## 🚀 Quick Commands

```bash
# Install FastAPI
pip install fastapi uvicorn

# Run development server
uvicorn main:app --reload

# View API docs
http://localhost:8000/docs

# Alternative docs
http://localhost:8000/redoc
```

---

## 📋 Interview Checklist

**Theory (15 mins):**
- [ ] Explain FastAPI advantages
- [ ] Difference from Flask/Django
- [ ] What is Pydantic?
- [ ] What is ASGI?
- [ ] Dependency injection concept

**Coding (30 mins):**
- [ ] Create basic endpoints
- [ ] Add request validation
- [ ] Implement error handling
- [ ] Use response models
- [ ] Database integration (if asked)

**Advanced (15 mins):**
- [ ] Background tasks
- [ ] Authentication basics
- [ ] Middleware concept
- [ ] Testing approach
- [ ] Deployment considerations

---

## 🎓 Study Plan (3 Days)

### Day 1: Basics
- Setup and Hello World
- Path and query parameters
- Request body with Pydantic
- Practice 5 simple endpoints

### Day 2: Intermediate
- Response models
- Error handling
- Dependency injection
- Database integration
- Build simple CRUD API

### Day 3: Practice
- Complete TODO app
- User management API
- Review error handling
- Practice explaining code
- Mock interview

---

## 📖 Resources

**Official Docs:**
- https://fastapi.tiangolo.com
- https://pydantic-docs.helpmanual.io

**Practice:**
- Build 3 small projects
- Contribute to open source
- Code review on GitHub

**YouTube:**
- FastAPI official playlist
- Real Python FastAPI course

---

## ⚡ Last Minute Review

**5 Things to Remember:**
1. Type hints are mandatory
2. Pydantic for validation
3. Depends() for dependencies
4. HTTPException for errors
5. response_model for output

**Common Patterns:**
```python
# Basic endpoint
@app.get("/")
def root():
    return {"message": "Hello"}

# With validation
class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create(item: Item):
    return item

# With database
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

---

**Good Luck! 🚀**

Remember: FastAPI is all about **type hints**, **validation**, and **automatic documentation**!
