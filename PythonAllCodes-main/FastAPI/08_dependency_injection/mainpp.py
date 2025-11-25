from fastapi import FastAPI, Depends
app = FastAPI()



def get_tokenwww():
    return "mysecrettoken"



@app.get("/protected/")
def protected_route():
    token = get_tokenwww()
    return {"token": token}



