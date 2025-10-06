from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

fake_users = {
    "alice": {"role": "admin"},
    "bob": {"role": "user"}
}

def get_current_user(username: str = ""):
    user = fake_users.get(username)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def require_admin(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user

@app.get("/admin/")
def admin_route(user=Depends(require_admin)):
    return {"message": "Welcome, admin!"}

@app.get("/user/")
def user_route(user=Depends(get_current_user)):
    return {"message": f"Welcome, {user['role']}!"}