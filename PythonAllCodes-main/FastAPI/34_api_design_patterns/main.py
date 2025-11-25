"""
API Design Patterns and Best Practices

This module demonstrates professional API design patterns essential for backend engineers:
- RESTful API design principles
- API versioning strategies
- Resource naming conventions
- HTTP status codes usage
- Error handling patterns
- Pagination strategies
- Response formatting standards
"""

from fastapi import FastAPI, HTTPException, Query, Path, Header, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum
import math

# API versioning strategy
API_VERSION = "v1"

app = FastAPI(
    title="Professional API Design Patterns",
    description="Demonstrates industry-standard API design patterns for backend engineers",
    version="1.0.0",
    openapi_prefix=f"/api/{API_VERSION}"
)

# Enums for consistent values
class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    suspended = "suspended"

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

# Standard response models
class ApiResponse(BaseModel):
    """Standard API response wrapper"""
    success: bool
    message: str
    data: Optional[Any] = None
    errors: Optional[List[str]] = None
    meta: Optional[Dict[str, Any]] = None

class PaginationMeta(BaseModel):
    """Pagination metadata"""
    page: int
    per_page: int
    total: int
    total_pages: int
    has_next: bool
    has_prev: bool

class PaginatedResponse(BaseModel):
    """Paginated response wrapper"""
    data: List[Any]
    meta: PaginationMeta

# Resource models
class UserBase(BaseModel):
    email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    full_name: str = Field(..., min_length=1, max_length=100)
    status: UserStatus = UserStatus.active

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    email: Optional[str] = Field(None, regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    full_name: Optional[str] = Field(None, min_length=1, max_length=100)
    status: Optional[UserStatus] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

# Mock database
users_db = []
next_user_id = 1

# Utility functions
def paginate_results(items: List, page: int, per_page: int) -> tuple:
    """Paginate results and return data + metadata"""
    total = len(items)
    total_pages = math.ceil(total / per_page) if per_page > 0 else 1
    start = (page - 1) * per_page
    end = start + per_page
    
    paginated_items = items[start:end]
    
    meta = PaginationMeta(
        page=page,
        per_page=per_page,
        total=total,
        total_pages=total_pages,
        has_next=page < total_pages,
        has_prev=page > 1
    )
    
    return paginated_items, meta

def create_success_response(data: Any, message: str = "Success", meta: Dict = None) -> ApiResponse:
    """Create standardized success response"""
    return ApiResponse(success=True, message=message, data=data, meta=meta)

def create_error_response(message: str, errors: List[str] = None) -> ApiResponse:
    """Create standardized error response"""
    return ApiResponse(success=False, message=message, errors=errors or [])

# API versioning middleware
@app.middleware("http")
async def add_api_version_header(request, call_next):
    response = await call_next(request)
    response.headers["X-API-Version"] = API_VERSION
    return response

# Health check endpoint
@app.get("/health", tags=["System"])
def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": API_VERSION,
        "service": "user-api"
    }

# Users resource endpoints following RESTful conventions
@app.post(
    "/users",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    summary="Create a new user",
    description="Creates a new user account with the provided information"
)
def create_user(user: UserCreate):
    """Create a new user following REST conventions"""
    global next_user_id
    
    # Check for duplicate email
    if any(u["email"] == user.email for u in users_db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )
    
    # Create user
    new_user = {
        "id": next_user_id,
        "email": user.email,
        "full_name": user.full_name,
        "status": user.status,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    users_db.append(new_user)
    next_user_id += 1
    
    return create_success_response(
        data=new_user,
        message="User created successfully"
    )

@app.get(
    "/users",
    response_model=ApiResponse,
    tags=["Users"],
    summary="List users with pagination and filtering"
)
def list_users(
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(10, ge=1, le=100, description="Items per page"),
    status: Optional[UserStatus] = Query(None, description="Filter by user status"),
    search: Optional[str] = Query(None, description="Search in name or email"),
    sort_by: str = Query("created_at", description="Sort field"),
    sort_order: SortOrder = Query(SortOrder.desc, description="Sort order")
):
    """List users with pagination, filtering, and sorting"""
    
    # Filter users
    filtered_users = users_db.copy()
    
    if status:
        filtered_users = [u for u in filtered_users if u["status"] == status]
    
    if search:
        search_lower = search.lower()
        filtered_users = [
            u for u in filtered_users 
            if search_lower in u["full_name"].lower() or search_lower in u["email"].lower()
        ]
    
    # Sort users
    reverse = sort_order == SortOrder.desc
    filtered_users.sort(
        key=lambda x: x.get(sort_by, ""),
        reverse=reverse
    )
    
    # Paginate results
    paginated_data, pagination_meta = paginate_results(filtered_users, page, per_page)
    
    return create_success_response(
        data=paginated_data,
        message="Users retrieved successfully",
        meta=pagination_meta.dict()
    )

@app.get(
    "/users/{user_id}",
    response_model=ApiResponse,
    tags=["Users"],
    summary="Get user by ID"
)
def get_user(
    user_id: int = Path(..., description="User ID", example=1)
):
    """Get a specific user by ID"""
    user = next((u for u in users_db if u["id"] == user_id), None)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    return create_success_response(
        data=user,
        message="User retrieved successfully"
    )

@app.put(
    "/users/{user_id}",
    response_model=ApiResponse,
    tags=["Users"],
    summary="Update user by ID"
)
def update_user(
    user_id: int = Path(..., description="User ID"),
    user_update: UserUpdate = None
):
    """Update a user by ID"""
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    
    if user_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    # Update only provided fields
    update_data = user_update.dict(exclude_unset=True)
    
    # Check for email conflicts
    if "email" in update_data:
        existing_user = next(
            (u for u in users_db if u["email"] == update_data["email"] and u["id"] != user_id), 
            None
        )
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists for another user"
            )
    
    # Apply updates
    users_db[user_index].update(update_data)
    users_db[user_index]["updated_at"] = datetime.utcnow()
    
    return create_success_response(
        data=users_db[user_index],
        message="User updated successfully"
    )

@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Users"],
    summary="Delete user by ID"
)
def delete_user(
    user_id: int = Path(..., description="User ID")
):
    """Delete a user by ID"""
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    
    if user_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    users_db.pop(user_index)
    return  # 204 No Content - empty response body

# Bulk operations endpoint
@app.post(
    "/users/bulk",
    response_model=ApiResponse,
    tags=["Users"],
    summary="Bulk create users"
)
def bulk_create_users(users: List[UserCreate]):
    """Bulk create multiple users"""
    global next_user_id
    
    if len(users) > 100:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Maximum 100 users allowed per bulk operation"
        )
    
    created_users = []
    errors = []
    
    for i, user in enumerate(users):
        # Check for duplicate email
        if any(u["email"] == user.email for u in users_db + created_users):
            errors.append(f"User {i+1}: Email {user.email} already exists")
            continue
        
        new_user = {
            "id": next_user_id,
            "email": user.email,
            "full_name": user.full_name,
            "status": user.status,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        
        created_users.append(new_user)
        next_user_id += 1
    
    # Add successful users to database
    users_db.extend(created_users)
    
    response_data = {
        "created_count": len(created_users),
        "error_count": len(errors),
        "created_users": created_users
    }
    
    if errors:
        response_data["errors"] = errors
    
    return create_success_response(
        data=response_data,
        message=f"Bulk operation completed: {len(created_users)} created, {len(errors)} errors"
    )

# API documentation endpoint
@app.get("/", tags=["Documentation"])
def api_info():
    """API information and documentation"""
    return {
        "service": "Professional API Design Demo",
        "version": API_VERSION,
        "description": "Demonstrates backend engineering API design patterns",
        "features": [
            "RESTful API design",
            "Consistent response formatting",
            "Comprehensive error handling",
            "Pagination and filtering",
            "API versioning",
            "Bulk operations",
            "Health checks",
            "OpenAPI documentation"
        ],
        "endpoints": {
            "documentation": "/docs",
            "health": "/health",
            "users": "/users",
            "bulk_operations": "/users/bulk"
        },
        "design_patterns": [
            "Resource-based URLs",
            "HTTP status codes",
            "Pagination metadata",
            "Error response consistency",
            "API versioning headers",
            "Request/response validation"
        ]
    }

# Global exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Global HTTP exception handler for consistent error responses"""
    return create_error_response(
        message=exc.detail,
        errors=[exc.detail]
    ).__dict__