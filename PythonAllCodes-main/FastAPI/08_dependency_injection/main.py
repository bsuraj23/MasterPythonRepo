from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

def get_token():
    # Simulate token retrieval (could be from headers, cookies, etc.)
    return "mysecrettoken"

def verify_token(token: str = Depends(get_token)):
    # Simulate token verification logic
    if token != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/protected2/")
def protected_route(token: str = Depends(get_token)):
    """
    Returns the token using dependency injection.
    """
    return {"token": token}

@app.get("/secure-data2/")
def secure_data(token: str = Depends(verify_token)):
    """
    Only accessible if token is valid.
    """
    return {"data": "This is secure data", "token": token}

def get_db():
    # Simulate a database session dependency
    db = {"users": ["alice", "bob", "carol"]}
    return db

@app.get("/users2/")
def list_users(db=Depends(get_db)):
    """
    Demonstrates dependency injection for database access.
    """
    return {"users": db["users"]}

def get_logger():
    # Simulate a logger dependency
    def log(message: str):
        print(f"LOG: {message}")
    return log

@app.post("/log/")
def log_message(message: str, logger=Depends(get_logger)):
    """
    Demonstrates dependency injection for logging.
    """
    logger(message)
    return {"logged": message}
