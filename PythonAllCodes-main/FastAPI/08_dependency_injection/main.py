"""
FastAPI Dependency Injection - Comprehensive Guide

This module demonstrates all aspects of dependency injection in FastAPI:
1. What are dependencies?
2. Creating and using dependencies
3. Common use cases (database, authentication, logging)
4. Using Depends() for cleaner code
5. Advanced dependency patterns
"""

from fastapi import FastAPI, Depends, HTTPException, Query
from typing import Optional, Annotated
import time

app = FastAPI(
    title="Dependency Injection Guide",
    description="Comprehensive examples of dependency injection in FastAPI"
)

# =============================================================================
# 1. BASIC DEPENDENCIES
# =============================================================================

def get_timestamp():
    """Simple dependency that returns current timestamp"""
    return int(time.time())

def get_user_agent(user_agent: str = None):
    """Dependency that extracts user agent from headers"""
    return user_agent or "Unknown"

@app.get("/basic-dependency")
def basic_example(timestamp: int = Depends(get_timestamp)):
    """Basic dependency injection example"""
    return {"message": "Basic dependency", "timestamp": timestamp}

# =============================================================================
# 2. COMMON USE CASES
# =============================================================================

# Database simulation
def get_db():
    """Simulate a database session dependency"""
    print("📊 Creating database connection...")
    db = {
        "users": ["alice", "bob", "charlie", "diana"],
        "products": ["laptop", "phone", "tablet"]
    }
    try:
        yield db
    finally:
        print("📊 Closing database connection...")

# Authentication simulation
def get_current_user(token: str = Query(None)):
    """Simulate user authentication dependency"""
    if not token:
        raise HTTPException(status_code=401, detail="Token required")
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "alice", "role": "admin"}

# Logging dependency
def get_logger():
    """Logger dependency"""
    def log(message: str, level: str = "INFO"):
        print(f"🔍 [{level}] {message}")
    return log

@app.get("/users/")
def list_users(
    db=Depends(get_db), 
    current_user=Depends(get_current_user),
    logger=Depends(get_logger)
):
    """Endpoint demonstrating multiple dependencies"""
    logger(f"User {current_user['username']} requested user list")
    return {
        "current_user": current_user,
        "users": db["users"],
        "total": len(db["users"])
    }

# =============================================================================
# 3. DEPENDS() FOR CLEANER CODE
# =============================================================================

def verify_admin_role(current_user=Depends(get_current_user)):
    """Dependency that verifies admin role"""
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

@app.get("/admin/users")
def admin_users(
    admin_user=Depends(verify_admin_role),
    db=Depends(get_db)
):
    """Admin-only endpoint using dependency for role verification"""
    return {
        "admin": admin_user["username"],
        "users": db["users"],
        "message": "Admin access granted"
    }

# =============================================================================
# 4. ADVANCED DEPENDENCY PATTERNS
# =============================================================================

# Dependency with parameters
def create_rate_limiter(requests_per_minute: int):
    """Factory function to create rate limiter dependency"""
    def rate_limiter():
        # In real app, you'd implement actual rate limiting
        return f"Rate limited to {requests_per_minute} requests/minute"
    return rate_limiter

# Sub-dependencies (dependencies that depend on other dependencies)
def get_user_permissions(current_user=Depends(get_current_user)):
    """Dependency that gets user permissions based on current user"""
    permissions = {
        "admin": ["read", "write", "delete"],
        "user": ["read"]
    }
    return permissions.get(current_user.get("role", "user"), ["read"])

def check_write_permission(permissions=Depends(get_user_permissions)):
    """Sub-dependency that checks write permission"""
    if "write" not in permissions:
        raise HTTPException(status_code=403, detail="Write permission required")
    return True

@app.post("/products/")
def create_product(
    product_name: str,
    has_write_permission=Depends(check_write_permission),
    db=Depends(get_db),
    logger=Depends(get_logger)
):
    """Endpoint with sub-dependencies"""
    logger(f"Creating product: {product_name}")
    db["products"].append(product_name)
    return {
        "message": "Product created",
        "product": product_name,
        "total_products": len(db["products"])
    }

# =============================================================================
# 5. DEPENDENCY INJECTION WITH CLASSES
# =============================================================================

class DatabaseService:
    """Database service class"""
    def __init__(self):
        self.connection = "mock-db-connection"
    
    def get_items(self):
        return ["item1", "item2", "item3"]
    
    def create_item(self, item: str):
        return f"Created {item} in database"

def get_database_service():
    """Dependency that returns database service instance"""
    return DatabaseService()

@app.get("/service-items/")
def get_items_with_service(db_service: DatabaseService = Depends(get_database_service)):
    """Using class-based dependency"""
    return {"items": db_service.get_items()}

# =============================================================================
# 6. OPTIONAL DEPENDENCIES
# =============================================================================

def get_optional_cache(use_cache: bool = Query(default=True)):
    """Optional caching dependency"""
    if use_cache:
        return {"cache": "enabled", "data": "cached_data"}
    return None

@app.get("/cached-data/")
def get_cached_data(cache=Depends(get_optional_cache)):
    """Endpoint with optional dependency"""
    if cache:
        return {"source": "cache", "data": cache["data"]}
    return {"source": "database", "data": "fresh_data"}

# =============================================================================
# 7. GLOBAL DEPENDENCIES
# =============================================================================

def log_requests():
    """Global dependency for request logging"""
    print("🌐 Global request logger activated")
    return "logged"

# Apply global dependency to all routes in this router
# app.dependencies = [Depends(log_requests)]  # Uncomment to enable global logging

# =============================================================================
# 8. UTILITY ENDPOINTS
# =============================================================================

@app.get("/")
def root():
    """Root endpoint with information about available examples"""
    return {
        "title": "FastAPI Dependency Injection Guide",
        "examples": {
            "basic": "/basic-dependency",
            "authentication": "/users/?token=valid-token",
            "admin": "/admin/users?token=valid-token",
            "rate_limited": "/rate-limited",
            "class_service": "/service-items/",
            "optional_cache": "/cached-data/?use_cache=true",
            "sub_dependencies": "POST /products/?token=valid-token"
        },
        "docs": "/docs"
    }

@app.get("/rate-limited")
def rate_limited_endpoint(
    rate_limit=Depends(create_rate_limiter(10))
):
    """Endpoint with factory-created dependency"""
    return {"message": "Success", "rate_limit": rate_limit}

# =============================================================================
# SUMMARY AND BEST PRACTICES
# =============================================================================

"""
DEPENDENCY INJECTION BEST PRACTICES:

1. REUSABILITY: Write dependencies that can be reused across multiple endpoints
2. SEPARATION OF CONCERNS: Keep authentication, database, logging separate
3. TESTABILITY: Dependencies make testing easier with dependency overrides
4. COMPOSABILITY: Build complex dependencies from simpler ones
5. TYPE HINTS: Use proper type hints for better IDE support
6. ERROR HANDLING: Handle errors appropriately in dependencies
7. RESOURCE CLEANUP: Use yield for dependencies that need cleanup
8. FACTORY PATTERN: Use factory functions for configurable dependencies

COMMON PATTERNS:
- Database sessions
- Authentication/Authorization
- Logging and monitoring
- Rate limiting
- Caching
- Configuration injection
- External service clients
"""



