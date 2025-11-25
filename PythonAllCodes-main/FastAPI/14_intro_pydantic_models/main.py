# Introduction to Pydantic models
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users/")
def create_user(user: User):
    if not user.name or user.age < 0:
        return {"error": "Invalid user data. Please provide valid name and positive age."}
    return {"message": "User created successfully", "user": user}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pydantic Models Example!"}   