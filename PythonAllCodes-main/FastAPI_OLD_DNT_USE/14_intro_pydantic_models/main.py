# Introduction to Pydantic models
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users/")
def create_user(user: User):
    return user


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pydantic Models Example!"}   