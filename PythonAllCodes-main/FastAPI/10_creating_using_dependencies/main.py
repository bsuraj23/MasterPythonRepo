# Creating and using dependencies in FastAPI
from fastapi import FastAPI, Depends

def get_query(query: str = None):
    return "Happy Birthday"

def xyz():
    return 123


app = FastAPI()


@app.get("/items/")
def read_items(query: str = Depends(get_query)):
    return {"query": query}


def add(a=9,b=1):
    return a+b


