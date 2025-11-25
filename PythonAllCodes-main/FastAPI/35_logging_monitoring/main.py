"""
Production Logging and Monitoring

This module demonstrates professional logging, monitoring, and observability patterns
essential for backend engineers in production environments.
"""

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import logging
import json
import time
import uuid
from datetime import datetime
from typing import Dict, Any, Optional
import sys
from contextlib import contextmanager
from pydantic import BaseModel
import traceback

# Configure structured logging
class JSONFormatter(logging.Formatter):
    """Custom JSON formatter for structured logging"""
    
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # Add exception info if present
        if record.exc_info:
            log_data["exception"] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1]),
                "traceback": traceback.format_exception(*record.exc_info)
            }
        
        # Add extra fields
        if hasattr(record, 'request_id'):
            log_data["request_id"] = record.request_id
        if hasattr(record, 'user_id'):
            log_data["user_id"] = record.user_id
        if hasattr(record, 'endpoint'):
            log_data["endpoint"] = record.endpoint
        if hasattr(record, 'duration_ms'):
            log_data["duration_ms"] = record.duration_ms
        
        return json.dumps(log_data)

# Setup logger
def setup_logger():
    """Configure application logger with JSON formatting"""
    logger = logging.getLogger("backend_api")
    logger.setLevel(logging.INFO)
    
    # Remove default handlers
    logger.handlers.clear()
    
    # Console handler with JSON formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(JSONFormatter())
    logger.addHandler(console_handler)
    
    return logger

# Application logger
app_logger = setup_logger()

# FastAPI app
app = FastAPI(
    title="Production Logging & Monitoring",
    description="Professional logging, monitoring, and observability patterns"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request context storage
request_context: Dict[str, Any] = {}

# Models
class LogLevel(BaseModel):
    level: str

class HealthStatus(BaseModel):
    status: str
    timestamp: str
    version: str
    uptime_seconds: float
    request_count: int
    error_count: int

# Metrics storage (in production, use Redis/InfluxDB/Prometheus)
metrics = {
    "request_count": 0,
    "error_count": 0,
    "total_duration_ms": 0,
    "endpoint_metrics": {},
    "start_time": time.time()
}

# Middleware for request tracking and logging
@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    """Comprehensive request/response logging middleware"""
    
    # Generate request ID
    request_id = str(uuid.uuid4())
    request_context["request_id"] = request_id
    
    # Start timing
    start_time = time.time()
    
    # Log request
    app_logger.info(
        f"Request started: {request.method} {request.url.path}",
        extra={
            "request_id": request_id,
            "method": request.method,
            "url": str(request.url),
            "client_ip": request.client.host,
            "user_agent": request.headers.get("user-agent"),
            "endpoint": f"{request.method} {request.url.path}"
        }
    )
    
    # Update metrics
    metrics["request_count"] += 1
    endpoint_key = f"{request.method} {request.url.path}"
    if endpoint_key not in metrics["endpoint_metrics"]:
        metrics["endpoint_metrics"][endpoint_key] = {"count": 0, "total_duration": 0, "errors": 0}
    
    metrics["endpoint_metrics"][endpoint_key]["count"] += 1
    
    try:
        # Process request
        response = await call_next(request)
        
        # Calculate duration
        duration_ms = (time.time() - start_time) * 1000
        metrics["total_duration_ms"] += duration_ms
        metrics["endpoint_metrics"][endpoint_key]["total_duration"] += duration_ms
        
        # Log response
        app_logger.info(
            f"Request completed: {request.method} {request.url.path}",
            extra={
                "request_id": request_id,
                "status_code": response.status_code,
                "duration_ms": round(duration_ms, 2),
                "endpoint": endpoint_key
            }
        )
        
        # Add headers
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Response-Time"] = str(round(duration_ms, 2))
        
        return response
        
    except Exception as e:
        # Calculate duration for failed requests
        duration_ms = (time.time() - start_time) * 1000
        
        # Update error metrics
        metrics["error_count"] += 1
        metrics["endpoint_metrics"][endpoint_key]["errors"] += 1
        
        # Log error
        app_logger.error(
            f"Request failed: {request.method} {request.url.path}",
            extra={
                "request_id": request_id,
                "error": str(e),
                "duration_ms": round(duration_ms, 2),
                "endpoint": endpoint_key
            },
            exc_info=True
        )
        
        raise

# Context manager for operation logging
@contextmanager
def log_operation(operation_name: str, **context):
    """Context manager for logging operations with timing"""
    request_id = request_context.get("request_id", "unknown")
    start_time = time.time()
    
    app_logger.info(
        f"Operation started: {operation_name}",
        extra={
            "request_id": request_id,
            "operation": operation_name,
            **context
        }
    )
    
    try:
        yield
        duration_ms = (time.time() - start_time) * 1000
        app_logger.info(
            f"Operation completed: {operation_name}",
            extra={
                "request_id": request_id,
                "operation": operation_name,
                "duration_ms": round(duration_ms, 2),
                **context
            }
        )
    except Exception as e:
        duration_ms = (time.time() - start_time) * 1000
        app_logger.error(
            f"Operation failed: {operation_name}",
            extra={
                "request_id": request_id,
                "operation": operation_name,
                "duration_ms": round(duration_ms, 2),
                "error": str(e),
                **context
            },
            exc_info=True
        )
        raise

# Dependency for user context
def get_current_user():
    """Mock user authentication for logging context"""
    # In real app, extract from JWT token
    return {"user_id": "user_123", "username": "john_doe"}

# Health check endpoint with metrics
@app.get("/health", response_model=HealthStatus, tags=["Monitoring"])
def health_check():
    """Comprehensive health check with metrics"""
    uptime = time.time() - metrics["start_time"]
    
    health_data = HealthStatus(
        status="healthy",
        timestamp=datetime.utcnow().isoformat(),
        version="1.0.0",
        uptime_seconds=round(uptime, 2),
        request_count=metrics["request_count"],
        error_count=metrics["error_count"]
    )
    
    app_logger.info("Health check performed", extra={"uptime_seconds": uptime})
    
    return health_data

# Metrics endpoint
@app.get("/metrics", tags=["Monitoring"])
def get_metrics():
    """Get detailed application metrics"""
    uptime = time.time() - metrics["start_time"]
    
    # Calculate average response time
    avg_response_time = (
        metrics["total_duration_ms"] / metrics["request_count"] 
        if metrics["request_count"] > 0 else 0
    )
    
    # Calculate endpoint-specific metrics
    endpoint_stats = {}
    for endpoint, stats in metrics["endpoint_metrics"].items():
        endpoint_stats[endpoint] = {
            "request_count": stats["count"],
            "error_count": stats["errors"],
            "error_rate": stats["errors"] / stats["count"] if stats["count"] > 0 else 0,
            "avg_duration_ms": stats["total_duration"] / stats["count"] if stats["count"] > 0 else 0
        }
    
    return {
        "uptime_seconds": round(uptime, 2),
        "total_requests": metrics["request_count"],
        "total_errors": metrics["error_count"],
        "error_rate": metrics["error_count"] / metrics["request_count"] if metrics["request_count"] > 0 else 0,
        "avg_response_time_ms": round(avg_response_time, 2),
        "endpoints": endpoint_stats
    }

# Business logic endpoints with comprehensive logging
@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: int, current_user: dict = Depends(get_current_user)):
    """Get user with comprehensive logging"""
    
    with log_operation("get_user", user_id=user_id, requested_by=current_user["user_id"]):
        # Simulate database operation
        if user_id <= 0:
            app_logger.warning(
                f"Invalid user ID requested: {user_id}",
                extra={
                    "request_id": request_context.get("request_id"),
                    "user_id": user_id,
                    "requested_by": current_user["user_id"]
                }
            )
            raise HTTPException(status_code=400, detail="Invalid user ID")
        
        if user_id > 1000:
            app_logger.warning(
                f"User not found: {user_id}",
                extra={
                    "request_id": request_context.get("request_id"),
                    "user_id": user_id,
                    "requested_by": current_user["user_id"]
                }
            )
            raise HTTPException(status_code=404, detail="User not found")
        
        # Simulate successful user retrieval
        user_data = {
            "id": user_id,
            "username": f"user_{user_id}",
            "email": f"user{user_id}@example.com"
        }
        
        app_logger.info(
            f"User retrieved successfully: {user_id}",
            extra={
                "request_id": request_context.get("request_id"),
                "user_id": user_id,
                "requested_by": current_user["user_id"]
            }
        )
        
        return user_data

@app.post("/users", tags=["Users"])
def create_user(user_data: dict, current_user: dict = Depends(get_current_user)):
    """Create user with audit logging"""
    
    with log_operation("create_user", created_by=current_user["user_id"], user_data=user_data):
        # Validate input
        if not user_data.get("username"):
            app_logger.warning(
                "User creation failed: missing username",
                extra={
                    "request_id": request_context.get("request_id"),
                    "created_by": current_user["user_id"],
                    "user_data": user_data
                }
            )
            raise HTTPException(status_code=400, detail="Username is required")
        
        # Simulate user creation
        new_user = {
            "id": 123,
            "username": user_data["username"],
            "email": user_data.get("email"),
            "created_at": datetime.utcnow().isoformat(),
            "created_by": current_user["user_id"]
        }
        
        app_logger.info(
            f"User created successfully: {new_user['id']}",
            extra={
                "request_id": request_context.get("request_id"),
                "user_id": new_user["id"],
                "username": new_user["username"],
                "created_by": current_user["user_id"]
            }
        )
        
        return new_user

# Error simulation endpoint
@app.get("/simulate-error", tags=["Testing"])
def simulate_error(error_type: str = "generic"):
    """Simulate different types of errors for testing logging"""
    
    app_logger.info(
        f"Simulating error: {error_type}",
        extra={
            "request_id": request_context.get("request_id"),
            "error_type": error_type
        }
    )
    
    if error_type == "validation":
        raise HTTPException(status_code=400, detail="Validation error simulated")
    elif error_type == "not_found":
        raise HTTPException(status_code=404, detail="Resource not found")
    elif error_type == "server":
        raise HTTPException(status_code=500, detail="Internal server error")
    elif error_type == "timeout":
        time.sleep(2)  # Simulate timeout
        raise HTTPException(status_code=504, detail="Gateway timeout")
    else:
        raise Exception("Generic exception simulated")

# Log level management
@app.post("/admin/log-level", tags=["Administration"])
def set_log_level(log_level: LogLevel):
    """Dynamically change log level"""
    level = getattr(logging, log_level.level.upper(), None)
    if level is None:
        raise HTTPException(status_code=400, detail="Invalid log level")
    
    app_logger.setLevel(level)
    
    app_logger.info(
        f"Log level changed to {log_level.level}",
        extra={
            "request_id": request_context.get("request_id"),
            "new_level": log_level.level
        }
    )
    
    return {"message": f"Log level set to {log_level.level}"}

# Structured logging examples
@app.get("/logging-examples", tags=["Examples"])
def logging_examples():
    """Demonstrate different logging patterns"""
    request_id = request_context.get("request_id")
    
    # Info logging with context
    app_logger.info(
        "Processing business logic",
        extra={
            "request_id": request_id,
            "step": "validation",
            "user_id": "user_123"
        }
    )
    
    # Debug logging (won't show unless level is DEBUG)
    app_logger.debug(
        "Debug information",
        extra={
            "request_id": request_id,
            "debug_data": {"key": "value"}
        }
    )
    
    # Warning logging
    app_logger.warning(
        "Deprecated API endpoint used",
        extra={
            "request_id": request_id,
            "endpoint": "/old-api",
            "replacement": "/new-api"
        }
    )
    
    return {
        "message": "Logging examples completed",
        "note": "Check the logs to see structured output"
    }

@app.get("/", tags=["Documentation"])
def root():
    """API documentation"""
    return {
        "service": "Production Logging & Monitoring Demo",
        "features": [
            "Structured JSON logging",
            "Request/response tracking",
            "Performance metrics",
            "Health checks",
            "Error tracking",
            "Operation logging",
            "Dynamic log levels",
            "Request correlation"
        ],
        "monitoring_endpoints": {
            "health": "/health",
            "metrics": "/metrics",
            "log_level": "/admin/log-level"
        },
        "logging_features": [
            "Request correlation IDs",
            "Structured JSON format",
            "Performance timing",
            "Error tracking with stack traces",
            "User context tracking",
            "Operation-level logging"
        ]
    }