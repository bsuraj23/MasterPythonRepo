from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_KEY = "mysecretkey"
api_key_header = APIKeyHeader(name="X-API-Key")

app = FastAPI()

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/secure-data/")
def secure_data(api_key: str = Depends(get_api_key)):
    return {"message": "You have access to secure data!"}