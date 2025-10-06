# Using Depends() for cleaner code
from fastapi import FastAPI, Depends

def get_token():
    return "xyz"

def example_for_depends():
    return "apple"

app = FastAPI()

@app.get("/secure/")
def secure_route_xyz(token: str = Depends(example_for_depends)):
    result = get_token()
    return { "token": result }
