# OAuth2 Password Flow Authentication Example

This project demonstrates OAuth2 password flow authentication in FastAPI.

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
   - Use `/token` to get a token (username: `alice`, password: `wonderland`)
   - Use `/users/me` with the token

## Notes

- This is a demo; in production, use JWT tokens and secure password storage.