# Using Depends() for cleaner code
from fastapi import FastAPI, Depends

def get_token():
    return "xyz"


def exnaple_for_depends():
    return "apple"

app = FastAPI()

@app.get("/secure/")
def secure_route(token: str = Depends(exnaple_for_depends)):
    return {"token": token}
