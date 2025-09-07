from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

def verify_token(token: str = ""):
    if token != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/open/")
def open_route():
    return {"message": "Anyone can access this route."}

@app.get("/protected/")
def protected_route(token: str = Depends(verify_token)):
    return {"message": "You are authorized!", "token": token}