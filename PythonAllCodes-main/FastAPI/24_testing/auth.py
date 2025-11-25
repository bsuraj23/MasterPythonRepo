from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

# Main application
app = FastAPI(title="Testing Demo API")


# Routes
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI testing!", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "items_count": len(items_db)}