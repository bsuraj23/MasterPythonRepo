# Creating Tables and Defining ORM Models with FastAPI & SQLAlchemy

This project demonstrates how to define ORM models and create tables in a database using SQLAlchemy with FastAPI.

## How to Run

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Start the FastAPI server:**
   ```powershell
   uvicorn main:app --reload
   ```

3. **Check the database:**
   - On first run, a file named `orm_demo.db` will be created in this folder.
   - The `products` table will be created automatically.

4. **Test the API:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - You should see a welcome message.

## Notes

- The ORM model is defined in the `Product` class.
- Tables are created using `Base.metadata.create_all(bind=engine)`.
- You can extend this example to add CRUD operations for the `Product` model.
```# filepath: c:\Users\Suraj\Desktop\GreenWorkSpace1\A2JulyWorkSpace\PythonAllCodes-main\FastAPI\26_orm_models\README.md
# Creating Tables and Defining ORM Models with FastAPI & SQLAlchemy

This project demonstrates how to define ORM models and create tables in a database using SQLAlchemy with FastAPI.

## How to Run

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Start the FastAPI server:**
   ```powershell
   uvicorn main:app --reload
   ```

3. **Check the database:**
   - On first run, a file named `orm_demo.db` will be created in this folder.
   - The `products` table will be created automatically.

4. **Test the API:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - You should see a welcome message.

## Notes

- The ORM model is defined in the `Product` class.
- Tables are created using `Base.metadata.create_all(bind=engine)`.
- You can extend this example to add CRUD operations for