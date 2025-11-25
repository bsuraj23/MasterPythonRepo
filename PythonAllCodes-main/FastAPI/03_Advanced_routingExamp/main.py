"""
Advanced FastAPI Routing Example

This module demonstrates advanced routing patterns including:
- External API integration
- Error handling
- Response models
- Multiple route types
- Path parameters
- Query parameters
"""

from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict, Any
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI(
    title="Advanced Routing Example",
    description="Demonstrates advanced routing patterns with external API integration",
    version="1.0.0"
)

# Response models
class HealthCheck(BaseModel):
    status: str
    message: str

class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to Advanced Routing API",
        "endpoints": {
            "health": "/health",
            "schemas": "/schemas",
            "schema_by_id": "/schemas/{schema_id}",
            "custom_request": "/api/request",
            "docs": "/docs"
        },
        "external_api": "https://data.healthcare.gov/api/1/metastore/schemas"
    }

# Health check endpoint
@app.get("/health", response_model=HealthCheck, tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return HealthCheck(
        status="healthy",
        message="API is running successfully"
    )

# External API integration with error handling
@app.get("/schemas", response_model=APIResponse, tags=["External API"])
async def get_schemas(
    limit: Optional[int] = Query(None, ge=1, le=100, description="Limit number of results")
):
    """
    Fetch schemas from external Healthcare.gov API
    
    This endpoint demonstrates:
    - External API integration
    - Error handling
    - Query parameters
    - Response validation
    
    Original curl command:
    ```
    curl -X 'GET' \
      'https://data.healthcare.gov/api/1/metastore/schemas' \
      -H 'accept: application/json'
    ```
    """
    try:
        url = "https://data.healthcare.gov/api/1/metastore/schemas"
        headers = {"accept": "application/json"}
        
        logger.info(f"Fetching schemas from: {url}")
        
        # Make request with timeout
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Apply limit if provided
        if limit and isinstance(data, list):
            data = data[:limit]
        
        logger.info(f"Successfully fetched {len(data) if isinstance(data, list) else 'data'}")
        
        return APIResponse(
            success=True,
            data=data
        )
        
    except requests.exceptions.Timeout:
        logger.error("Request timeout")
        raise HTTPException(status_code=504, detail="External API request timed out")
    
    except requests.exceptions.ConnectionError:
        logger.error("Connection error")
        raise HTTPException(status_code=503, detail="Cannot connect to external API")
    
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=502, detail=f"External API error: {str(e)}")
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return APIResponse(
            success=False,
            error=f"An unexpected error occurred: {str(e)}"
        )

# Get specific schema by ID
@app.get("/schemas/{schema_id}", response_model=APIResponse, tags=["External API"])
async def get_schema_by_id(
    schema_id: str = Path(..., description="Schema identifier")
):
    """
    Fetch a specific schema by ID from external API
    
    Path parameter example: /schemas/abc-123
    """
    try:
        url = f"https://data.healthcare.gov/api/1/metastore/schemas/{schema_id}"
        headers = {"accept": "application/json"}
        
        logger.info(f"Fetching schema {schema_id}")
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        return APIResponse(
            success=True,
            data=response.json()
        )
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Schema {schema_id} not found")
        raise HTTPException(status_code=502, detail=f"External API error: {str(e)}")
    
    except Exception as e:
        logger.error(f"Error fetching schema: {e}")
        return APIResponse(
            success=False,
            error=str(e)
        )

# Custom external API request
@app.get("/api/request", tags=["External API"])
async def custom_api_request(
    url: str = Query(..., description="External API URL to request"),
    method: str = Query("GET", description="HTTP method"),
    timeout: int = Query(10, ge=1, le=30, description="Request timeout in seconds")
):
    """
    Make a custom request to any external API
    
    Query parameters:
    - url: The external API endpoint
    - method: HTTP method (GET, POST, etc.)
    - timeout: Request timeout in seconds
    
    Example: /api/request?url=https://api.github.com/users/github
    """
    try:
        if method.upper() not in ["GET", "POST", "PUT", "DELETE"]:
            raise HTTPException(status_code=400, detail="Invalid HTTP method")
        
        logger.info(f"Making {method} request to: {url}")
        
        response = requests.request(
            method=method.upper(),
            url=url,
            headers={"accept": "application/json"},
            timeout=timeout
        )
        response.raise_for_status()
        
        return {
            "success": True,
            "status_code": response.status_code,
            "data": response.json() if response.text else None
        }
        
    except requests.exceptions.JSONDecodeError:
        return {
            "success": True,
            "status_code": response.status_code,
            "data": response.text,
            "note": "Response is not JSON format"
        }
    
    except Exception as e:
        logger.error(f"Request failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Example endpoint with multiple parameters
@app.get("/advanced/{item_id}", tags=["Advanced"])
async def advanced_routing(
    item_id: int = Path(..., ge=1, description="Item ID (must be >= 1)"),
    q: Optional[str] = Query(None, min_length=3, max_length=50, description="Search query"),
    skip: int = Query(0, ge=0, description="Skip items"),
    limit: int = Query(10, ge=1, le=100, description="Limit results")
):
    """
    Advanced routing example with path and query parameters
    
    - Path parameter: item_id (required)
    - Query parameters: q, skip, limit (optional)
    
    Example: /advanced/5?q=test&skip=10&limit=20
    """
    return {
        "item_id": item_id,
        "query": q,
        "pagination": {
            "skip": skip,
            "limit": limit
        },
        "message": "Advanced routing with multiple parameters"
    }

if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server...")
    print("API Documentation: http://127.0.0.1:8000/docs")
    print("Root endpoint: http://127.0.0.1:8000/")
    print("Schemas endpoint: http://127.0.0.1:8000/schemas")
    uvicorn.run(app, host="127.0.0.1", port=8000) 
