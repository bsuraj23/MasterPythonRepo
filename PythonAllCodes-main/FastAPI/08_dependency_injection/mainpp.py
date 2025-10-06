from fastapi import FastAPI, Depends

def get_tokenwww():
    return "mysecrettoken"

app = FastAPI()

@app.get("/protected/")
def protected_route(token: str = Depends(get_tokenwww)):
    return {"token": token}



