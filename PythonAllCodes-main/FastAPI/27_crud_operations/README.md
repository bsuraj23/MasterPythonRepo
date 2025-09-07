# FastAPI CRUD Operations Example

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using FastAPI and SQLAlchemy.

## How to Run

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Start the FastAPI server:**
   ```powershell
   uvicorn main:app --reload
   ```

3. **Test the API:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser for interactive API docs.

## Endpoints

- `POST /products/`  
  Create a new product.

- `GET /products/`  
  List all products.

- `GET /products/{product_id}`  
  Get a product by ID.

- `PUT /products/{product_id}`  
  Update a product by ID.

- `DELETE /products/{product_id}`  
  Delete a product by ID.

## Notes

- The database file `crud_demo.db` will be created automatically.
- All endpoints use SQLAlchemy ORM models and Pydantic schemas for validation.
```# filepath: c:\Users\Suraj\Desktop\GreenWorkSpace1\A2JulyWorkSpace\PythonAllCodes-main\FastAPI\27_crud_operations\README.md
# FastAPI CRUD Operations Example

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using FastAPI and SQLAlchemy.

## How to Run

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Start the FastAPI server:**
   ```powershell
   uvicorn main:app --reload
   ```

3. **Test the API:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser for interactive API docs.

## Endpoints

- `POST /products/`  
  Create a new product.

- `GET /products/`  
  List all products.

- `GET /products/{product_id}`  
  Get a product by ID.

- `PUT /products/{product_id}`  
  Update a product by ID.

- `DELETE /products/{product_id}`  
  Delete a product by ID.

## Notes

- The database file `crud_demo.db` will be created automatically.
- All endpoints use SQLAlchemy ORM models and Pydantic schemas