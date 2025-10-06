from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.post("/upload/")
def upload_file(name: str = Form(...), file: UploadFile = File(...)):
    return {"filename": file.filename, "name": name}