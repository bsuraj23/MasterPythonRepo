from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id,
            "user_name": "xyz"}

@app.get("/products/{product_id}")
def read_product(product_id: str):
    return {"product_id": product_id}

@app.get("/users/")
def read_all_users():
    # Example static list of users
    users = [
        {"user_id": 1, "name": "Alice"},
        {"user_id": 2, "name": "Bob"},
        {"user_id": 3, "name": "Charlie"}
    ]
    return {"users": users}

