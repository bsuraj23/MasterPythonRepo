from fastapi import FastAPI, Response, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn
import jwt
import datetime
import hashlib
import secrets
import os
from dotenv import load_dotenv
from authlib.integrations.starlette_client import OAuth
import httpx

# Load environment variables
load_dotenv()

app = FastAPI(title="FastAPI Backend with Cookies & Google OAuth", version="1.0.0", description="A FastAPI backend with cookie-based authentication and Google OAuth")

# Secret key for JWT tokens and session management
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this-in-production")
ALGORITHM = "HS256"

# Google OAuth Configuration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/auth/google/callback")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# Initialize OAuth
oauth = OAuth()
if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url='https://accounts.google.com/.well-known/openid_configuration',
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

# Simple in-memory storage for demo (use database in production)
users_db = {
    "testuser": {
        "username": "testuser",
        "password": "testpass123",  # In production, store hashed passwords
        "email": "test@example.com",
        "full_name": "Test User",
        "auth_provider": "local"
    }
}

# Active sessions storage (use Redis or database in production)
active_sessions = {}

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,  # Important for cookies
    allow_methods=["*"],
    allow_headers=["*"],
)

# Response models
class HelloResponse(BaseModel):
    message: str
    status: str
    data: Dict[str, Any]

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    message: str
    user: Dict[str, Any]
    session_id: str

class UserResponse(BaseModel):
    username: str
    email: str
    full_name: str
    auth_provider: str = "local"

class GoogleAuthResponse(BaseModel):
    message: str
    user: Dict[str, Any]
    session_id: str
    auth_provider: str

# Utility functions
def create_session_token(username: str) -> str:
    """Create a session token for the user"""
    session_data = {
        "username": username,
        "created_at": datetime.datetime.utcnow().isoformat(),
        "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(hours=24)).isoformat()
    }
    return jwt.encode(session_data, SECRET_KEY, algorithm=ALGORITHM)

def verify_session_token(token: str) -> Optional[Dict]:
    """Verify and decode session token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expires_at = datetime.datetime.fromisoformat(payload.get("expires_at"))
        if datetime.datetime.utcnow() > expires_at:
            return None
        return payload
    except jwt.InvalidTokenError:
        return None

def get_current_user(request: Request) -> Optional[Dict]:
    """Get current user from session cookie"""
    session_token = request.cookies.get("session_token")
    if not session_token:
        return None
    
    session_data = verify_session_token(session_token)
    if not session_data:
        return None
    
    username = session_data.get("username")
    if username in users_db:
        return users_db[username]
    return None

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "FastAPI Backend with Cookies & Google OAuth is running!", 
        "version": "1.0.0",
        "google_oauth_configured": GOOGLE_CLIENT_ID is not None
    }

@app.get("/auth/google")
async def google_auth(request: Request):
    """Initiate Google OAuth login"""
    if not GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=500, detail="Google OAuth not configured")
    
    redirect_uri = GOOGLE_REDIRECT_URI
    return await oauth.google.authorize_redirect(request, redirect_uri)

@app.get("/auth/google/callback")
async def google_callback(request: Request, response: Response):
    """Handle Google OAuth callback"""
    if not GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=500, detail="Google OAuth not configured")
    
    try:
        # Get the authorization token
        token = await oauth.google.authorize_access_token(request)
        
        # Get user info from Google
        user_info = token.get('userinfo')
        if not user_info:
            # If userinfo is not in token, fetch it manually
            async with httpx.AsyncClient() as client:
                user_response = await client.get(
                    'https://www.googleapis.com/oauth2/v2/userinfo',
                    headers={'Authorization': f'Bearer {token["access_token"]}'}
                )
                user_info = user_response.json()
        
        # Extract user information
        email = user_info.get('email')
        name = user_info.get('name', email)
        google_id = user_info.get('id')
        
        if not email:
            raise HTTPException(status_code=400, detail="Could not get user email from Google")
        
        # Create or update user in database
        username = f"google_{google_id}"
        users_db[username] = {
            "username": username,
            "email": email,
            "full_name": name,
            "google_id": google_id,
            "auth_provider": "google",
            "profile_picture": user_info.get('picture')
        }
        
        # Create session token
        session_token = create_session_token(username)
        
        # Store session
        session_id = secrets.token_urlsafe(32)
        active_sessions[session_id] = {
            "username": username,
            "created_at": datetime.datetime.utcnow(),
            "token": session_token,
            "auth_provider": "google"
        }
        
        # Set secure cookie
        response = RedirectResponse(url=f"{FRONTEND_URL}?auth=success")
        response.set_cookie(
            key="session_token",
            value=session_token,
            max_age=86400,  # 24 hours
            httponly=True,  # Prevent XSS attacks
            secure=False,   # Set to True in production with HTTPS
            samesite="lax"  # CSRF protection
        )
        
        return response
        
    except Exception as e:
        # Redirect to frontend with error
        return RedirectResponse(url=f"{FRONTEND_URL}?auth=error&message={str(e)}")

@app.get("/auth/google/url")
async def get_google_auth_url():
    """Get Google OAuth URL for frontend"""
    if not GOOGLE_CLIENT_ID:
        return {"google_auth_url": None, "configured": False}
    
    return {
        "google_auth_url": f"http://localhost:8000/auth/google",
        "configured": True
    }

@app.post("/api/login", response_model=LoginResponse)
async def login(login_data: LoginRequest, response: Response):
    """User login with cookie-based session"""
    username = login_data.username
    password = login_data.password
    
    # Check if user exists and password is correct
    if username not in users_db or users_db[username]["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    # Create session token
    session_token = create_session_token(username)
    
    # Store session (in production, use Redis or database)
    session_id = secrets.token_urlsafe(32)
    active_sessions[session_id] = {
        "username": username,
        "created_at": datetime.datetime.utcnow(),
        "token": session_token
    }
    
    # Set secure cookie
    response.set_cookie(
        key="session_token",
        value=session_token,
        max_age=86400,  # 24 hours
        httponly=True,  # Prevent XSS attacks
        secure=False,   # Set to True in production with HTTPS
        samesite="lax"  # CSRF protection
    )
    
    user_data = {
        "username": users_db[username]["username"],
        "email": users_db[username]["email"],
        "full_name": users_db[username]["full_name"]
    }
    
    return LoginResponse(
        message="Login successful",
        user=user_data,
        session_id=session_id
    )

@app.post("/api/logout")
async def logout(request: Request, response: Response):
    """User logout - clear session cookie"""
    session_token = request.cookies.get("session_token")
    
    # Remove session from active sessions
    if session_token:
        for session_id, session_data in list(active_sessions.items()):
            if session_data.get("token") == session_token:
                del active_sessions[session_id]
                break
    
    # Clear cookie
    response.delete_cookie(key="session_token", path="/")
    
    return {"message": "Logout successful"}

@app.get("/api/me", response_model=UserResponse)
async def get_current_user_info(request: Request):
    """Get current user information from session cookie"""
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    return UserResponse(
        username=user["username"],
        email=user["email"],
        full_name=user["full_name"],
        auth_provider=user.get("auth_provider", "local")
    )

@app.get("/api/hello", response_model=HelloResponse)
async def hello_world(request: Request):
    """Hello World GET API endpoint with user context"""
    user = get_current_user(request)
    
    if user:
        message = f"Hello {user['full_name']}! Welcome back to FastAPI!"
        user_data = {
            "username": user["username"],
            "email": user["email"],
            "authenticated": True
        }
    else:
        message = "Hello World from FastAPI! (Guest user)"
        user_data = {"authenticated": False}
    
    return HelloResponse(
        message=message,
        status="success",
        data={
            "backend": "FastAPI",
            "frontend": "React",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "user": user_data,
            "cookies_enabled": True
        }
    )

@app.get("/api/status")
async def get_status(request: Request):
    """API status endpoint with session info"""
    user = get_current_user(request)
    
    return {
        "status": "online",
        "message": "FastAPI backend is running successfully",
        "authenticated": user is not None,
        "user": user["username"] if user else None,
        "active_sessions": len(active_sessions),
        "google_oauth_configured": GOOGLE_CLIENT_ID is not None,
        "endpoints": [
            "/",
            "/auth/google",
            "/auth/google/callback",
            "/auth/google/url",
            "/api/login",
            "/api/logout", 
            "/api/me",
            "/api/hello",
            "/api/status",
            "/api/sessions",
            "/docs",
            "/redoc"
        ]
    }

@app.get("/api/sessions")
async def get_active_sessions(request: Request):
    """Get active sessions (admin endpoint - simplified for demo)"""
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # In production, add proper admin role checking
    sessions_info = []
    for session_id, session_data in active_sessions.items():
        sessions_info.append({
            "session_id": session_id[:8] + "...",  # Truncated for security
            "username": session_data["username"],
            "created_at": session_data["created_at"].isoformat(),
            "active": True
        })
    
    return {
        "total_sessions": len(active_sessions),
        "sessions": sessions_info
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)