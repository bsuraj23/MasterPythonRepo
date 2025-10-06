from fastapi import FastAPI

app = FastAPI()

@app.get("/xyz")
def read_root():
    return {"message": "Welcomedffsfdsfesf to FastAPI! Server is respoding successfully."}



@app.get("/23docs")
def get_docs():
    return {"docs_url": "http://127.0.0.1:8000/docs"}
