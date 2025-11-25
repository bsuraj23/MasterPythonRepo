# FastAPI Database Integration (PostgreSQL/MySQL/SQLite)

This project demonstrates comprehensive database integration with FastAPI, including PostgreSQL, MySQL, and SQLite support with production-ready patterns.

## Features

### Database Support
- **PostgreSQL**: Full support with psycopg2-binary driver
- **MySQL**: Complete integration with pymysql driver  
- **SQLite**: Development fallback (no additional setup required)
- **Environment Variables**: Flexible configuration for different environments

### API Features
- **Complete CRUD Operations**: Create, Read, Update, Delete with proper error handling
- **Pagination & Filtering**: Efficient data retrieval with search capabilities
- **Soft Delete**: Mark items as inactive instead of permanent deletion
- **Health Checks**: Database connectivity monitoring
- **Statistics**: Real-time database metrics and analytics

### Production-Ready Features
- **Connection Pooling**: Optimized database connection management
- **Error Handling**: Comprehensive exception handling and logging
- **Data Validation**: Strong input validation with Pydantic
- **Transaction Management**: Proper database transaction handling
- **Logging**: Structured logging for monitoring and debugging

## Prerequisites

- Python 3.8+
- Database server (optional - SQLite works out of the box)

## Quick Start

### 1. Install Dependencies
```powershell
# Install all dependencies
pip install -r requirements.txt
```

### 2. Run the Application (SQLite - No setup required)
```powershell
uvicorn main:app --reload
```

The API will be available at:
- **Swagger UI**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## API Endpoints

### Health & Monitoring
- `GET /health` - Database connectivity check
- `GET /stats` - Database statistics and metrics
- `GET /categories` - Get all item categories

### Item Management (Full CRUD)
- `POST /items/` - Create new item
- `GET /items/` - List items with pagination and filtering
- `GET /items/{item_id}` - Get specific item
- `PUT /items/{item_id}` - Update item
- `DELETE /items/{item_id}` - Soft delete item  
- `DELETE /items/{item_id}/permanent` - Permanently delete item

## Testing the Application

### 1. Start the Server
```powershell
uvicorn main:app --reload
```

### 2. Test Health Check
Visit: http://localhost:8000/health

### 3. Test API with Swagger UI
Visit: http://localhost:8000/docs

### 4. Or use curl commands
```powershell
# Health check
curl http://localhost:8000/health

# Create an item
curl -X POST "http://localhost:8000/items/" -H "Content-Type: application/json" -d '{\"name\": \"Test Item\", \"description\": \"A test item\", \"price\": \"19.99\", \"category\": \"test\"}'

# Get all items
curl "http://localhost:8000/items/"

# Get statistics
curl "http://localhost:8000/stats"
```

## Database Configuration (Optional)

The application uses SQLite by default. For PostgreSQL or MySQL:

### Environment Variables
```powershell
$env:DB_TYPE = "postgresql"  # or "mysql"
$env:DB_USER = "your_username"
$env:DB_PASSWORD = "your_password" 
$env:DB_HOST = "localhost"
$env:DB_PORT = "5432"  # or 3306 for MySQL
$env:DB_NAME = "your_database"
```

## Learning Objectives

1. **Database Integration**: Multi-database support patterns
2. **CRUD Operations**: Complete Create, Read, Update, Delete functionality
3. **Error Handling**: Production-ready exception management
4. **API Design**: RESTful endpoint design with pagination
5. **Data Validation**: Input validation with Pydantic models
6. **Monitoring**: Health checks and application metrics