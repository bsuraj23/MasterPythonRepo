# Protecting Routes with Depends Example

This project demonstrates how to protect FastAPI routes using dependency injection.

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
   - `/open/` is accessible to anyone.
   - `/protected/` requires a token query parameter:  
     Example: `/protected/?token=mysecrettoken`

## Notes

- In production, use real authentication and token verification.