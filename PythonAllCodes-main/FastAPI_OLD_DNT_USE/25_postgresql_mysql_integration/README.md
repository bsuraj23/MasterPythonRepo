# FastAPI PostgreSQL/MySQL Integration Example

This project demonstrates how to connect FastAPI to a PostgreSQL or MySQL database using SQLAlchemy.

## Prerequisites

- Python 3.8+
- PostgreSQL or MySQL server running locally or remotely
- Database and user created (update credentials in `main.py`)

## Setup

1. **Clone this repository or copy the folder.**

2. **Install dependencies:**

   For PostgreSQL:
   ```powershell
   pip install fastapi uvicorn sqlalchemy psycopg2-binary
   ```

   For MySQL:
   ```powershell
   pip install fastapi uvicorn sqlalchemy pymysql
   ```

3. **Update the database URL in `main.py`:**

   - For PostgreSQL:
     ```
     DATABASE_URL = "postgresql://<user>:<password>@localhost:5432/<dbname>"
     ```
   - For MySQL:
     ```
     DATABASE_URL = "mysql+pymysql://<user>:<password>@localhost:3306/<dbname>"
     ```

4. **Create the database tables:**

   Tables are created automatically on first run using SQLAlchemy's `Base.metadata.create_all()`.

## Running the Server

```powershell
uvicorn main:app --reload
```

## API Endpoints

- `POST /items/`  
  Create a new item.  
  Request body:  
  ```json
  {
    "name": "Item name",
    "description": "Item description"
  }
  ```

- `GET /items/`  
  Get all items.

- `GET /items/{item_id}`  
  Get a specific item by ID.

## Testing

You can test the API using:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- curl, Postman, or any HTTP client

## Notes

- Make sure your database server is running and accessible.
- The first run will create the `items` table if it does not exist.
- For production, use environment variables for credentials and consider Alembic for migrations.

---
```# filepath: c:\Users\Suraj\Desktop\GreenWorkSpace1\A2JulyWorkSpace\PythonAllCodes-main\FastAPI\25_postgresql_mysql_integration\README.md
# FastAPI PostgreSQL/MySQL Integration Example

This project demonstrates how to connect FastAPI to a PostgreSQL or MySQL database using SQLAlchemy.

## Prerequisites

- Python 3.8+
- PostgreSQL or MySQL server running locally or remotely
- Database and user created (update credentials in `main.py`)

## Setup

1. **Clone this repository or copy the folder.**

2. **Install dependencies:**

   For PostgreSQL:
   ```powershell
   pip install fastapi uvicorn sqlalchemy psycopg2-binary
   ```

   For MySQL:
   ```powershell
   pip install fastapi uvicorn sqlalchemy pymysql
   ```

3. **Update the database URL in `main.py`:**

   - For PostgreSQL:
     ```
     DATABASE_URL = "postgresql<user>:<password>@localhost:5432/<dbname>"
     ```
   - For MySQL:
     ```
     DATABASE_URL = "mysql+pymysql://<user>:<password>@localhost:3306/<dbname>"
     ```

4. **Create the database tables:**

   Tables are created automatically on first run using SQLAlchemy's `Base.metadata.create_all()`.

## Running the Server

```powershell
uvicorn main:app --reload
```

## API Endpoints

- `POST /items/`  
  Create a new item.  
  Request body:  
  ```json
  {
    "name": "Item name",
    "description": "Item description"
  }
  ```

- `GET /items/`  
  Get all items.

- `GET /items/{item_id}`  
  Get a specific item by ID.

## Testing

You can test the API using:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- curl, Postman, or any HTTP client

## Notes

- Make sure your database server is running and accessible.
- The first run will create the `items` table if it does not exist.
- For production, use environment variables for credentials and consider Alembic for migrations.