from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/token", data={"username": "alice", "password": "wonderland"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["access_token"] == "alice"
    assert data["token_type"] == "bearer"

def test_login_failure():
    response = client.post("/token", data={"username": "alice", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"

def test_read_users_me_success():
    # First, get a token
    token_resp = client.post("/token", data={"username": "alice", "password": "wonderland"})
    token = token_resp.json()["access_token"]
    # Use token to access protected endpoint
    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"username": "alice"}

def test_read_users_me_invalid_token():
    response = client.get("/users/me", headers={"Authorization": "Bearer invalidtoken"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid authentication credentials"

def test_read_users_me_missing_token():
    response = client.get("/users/me")
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]