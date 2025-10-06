# API Key Authentication Example

This project demonstrates API key authentication in FastAPI.

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
   - Use `/secure-data/` with header `X-API-Key: mysecretkey`

## Notes

- In production, store API keys securely and rotate them regularly.