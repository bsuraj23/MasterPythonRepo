# Alembic Database Migrations Example

This project demonstrates how to use Alembic for database migrations with FastAPI and SQLAlchemy.

## How to Run

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Initialize Alembic:**
   ```powershell
   alembic init alembic
   ```

3. **Edit `alembic/env.py` to use the same `DATABASE_URL` as in `main.py`.**

4. **Create a migration:**
   ```powershell
   alembic revision --autogenerate -m "create users table"
   ```

5. **Apply the migration:**
   ```powershell
   alembic upgrade head
   ```

6. **Start the FastAPI server:**
   ```powershell
   uvicorn main:app --reload
   ```

## Notes

- Alembic manages database schema changes.
- Do not use `Base.metadata.create_all()` in production; let Alembic handle migrations.