# FastAPI Backend

A simple FastAPI backend that provides REST APIs for the React frontend.

## Features

- Hello World GET API
- CORS enabled for React frontend
- API documentation with Swagger UI
- Status endpoint for health checks

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints

- `GET /` - Root endpoint
- `GET /api/hello` - Hello World API
- `GET /api/status` - API status
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Future Features

- Authentication & Authorization
- Cookie management
- Database integration
- User management
- JWT tokens