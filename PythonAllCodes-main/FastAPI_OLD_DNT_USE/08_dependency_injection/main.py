from fastapi import FastAPI, Depends

def get_token():
    return "mysecrettoken"

app = FastAPI()

@app.get("/protected/")
def protected_route(token: str = Depends(get_token)):
    return {"token": token}



