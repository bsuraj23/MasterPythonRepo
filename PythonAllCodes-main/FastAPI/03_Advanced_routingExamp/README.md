# Advanced FastAPI Routing Example

This project demonstrates advanced routing patterns in FastAPI including external API integration, error handling, path parameters, query parameters, and response models.

## Features

- **External API Integration**: Fetch data from Healthcare.gov API
- **Error Handling**: Comprehensive error handling for external requests
- **Path Parameters**: Dynamic routes with validation
- **Query Parameters**: Filtering and pagination support
- **Response Models**: Structured responses using Pydantic
- **Logging**: Built-in logging for debugging
- **API Documentation**: Auto-generated Swagger UI

## Installation

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

## Running the Server

### Option 1: Using uvicorn directly
```powershell
uvicorn main:app --reload
```

### Option 2: Using the run script
```powershell
python run_server.py
```

### Option 3: Run main.py directly
```powershell
python main.py
```

## API Endpoints

### Root Endpoint
- **GET /** - API information and available endpoints

### Health Check
- **GET /health** - Check API health status

### External API Integration
- **GET /schemas** - Fetch all schemas from Healthcare.gov API
  - Query params: `limit` (optional, 1-100)
  - Example: `/schemas?limit=10`

- **GET /schemas/{schema_id}** - Fetch specific schema by ID
  - Path param: `schema_id` (required)
  - Example: `/schemas/abc-123`

### Custom API Request
- **GET /api/request** - Make custom external API requests
  - Query params:
    - `url` (required) - External API URL
    - `method` (optional, default: GET)
    - `timeout` (optional, default: 10, range: 1-30)
  - Example: `/api/request?url=https://api.github.com/users/github`

### Advanced Routing
- **GET /advanced/{item_id}** - Advanced routing with multiple parameters
  - Path param: `item_id` (required, >= 1)
  - Query params:
    - `q` (optional, 3-50 chars) - Search query
    - `skip` (optional, >= 0) - Skip items
    - `limit` (optional, 1-100) - Limit results
  - Example: `/advanced/5?q=test&skip=10&limit=20`

## Testing the API

### Using Browser
1. Start the server
2. Visit: http://127.0.0.1:8000/docs
3. Try the interactive API documentation

### Using curl

```bash
# Get all schemas
curl http://127.0.0.1:8000/schemas

# Get schemas with limit
curl "http://127.0.0.1:8000/schemas?limit=5"

# Get specific schema
curl http://127.0.0.1:8000/schemas/abc-123

# Custom API request
curl "http://127.0.0.1:8000/api/request?url=https://api.github.com/users/github"

# Advanced routing
curl "http://127.0.0.1:8000/advanced/5?q=test&limit=10"

# Health check
curl http://127.0.0.1:8000/health
```

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Key Concepts Demonstrated

### 1. External API Integration
```python
@app.get("/schemas")
async def get_schemas():
    response = requests.get(url, headers=headers, timeout=10)
    return response.json()
```

### 2. Error Handling
```python
try:
    response.raise_for_status()
except requests.exceptions.Timeout:
    raise HTTPException(status_code=504, detail="Request timed out")
```

### 3. Path Parameters
```python
@app.get("/schemas/{schema_id}")
async def get_schema_by_id(schema_id: str = Path(...)):
    # schema_id is extracted from URL path
```

### 4. Query Parameters
```python
@app.get("/schemas")
async def get_schemas(
    limit: Optional[int] = Query(None, ge=1, le=100)
):
    # limit is extracted from query string
```

## Learning Objectives

- How to integrate external APIs in FastAPI
- Proper error handling for HTTP requests
- Path and query parameter validation
- Response model design
- API documentation with Swagger
- Logging best practices
