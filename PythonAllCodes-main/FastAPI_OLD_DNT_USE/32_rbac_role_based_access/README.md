# Role-Based Access Control (RBAC) Example

This project demonstrates RBAC in FastAPI using dependency injection.

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
   - `/admin/?username=alice` (admin access)
   - `/user/?username=bob` (user access)

## Notes

- In production, use real authentication and user management.