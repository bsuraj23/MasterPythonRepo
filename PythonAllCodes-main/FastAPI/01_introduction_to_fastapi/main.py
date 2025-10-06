from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI! today is Thursday  Server is responding successfully."}
    



@app.get("/name")
def get_name():
    return "Hansraj - FastAPI Developer"



#docs
@app.get("/docs")
def get_documentation():
    return "http://localhost:8000/docs"
    