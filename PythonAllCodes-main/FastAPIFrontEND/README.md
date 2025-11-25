# React + FastAPI Full Stack Project

A complete full-stack application with React frontend and FastAPI backend.

## Project Structure

```
FastAPIFrontEND/
├── my-react-app/                 # React Frontend
│   ├── src/
│   │   ├── App.jsx              # Main React component with API integration
│   │   └── index.jsx            # React app entry point
│   ├── public/
│   │   └── index.html           # HTML template
│   ├── package.json             # Node dependencies
│   └── README.md
├── fastapi-backend/             # FastAPI Backend
│   ├── main.py                  # FastAPI application
│   ├── requirements.txt         # Python dependencies
│   └── README.md
├── .venv/                       # Python virtual environment
└── README.md                    # This file
```

## Quick Setup for Google OAuth

### 1. Configure Google OAuth (Optional)
If you want to enable Google OAuth login:
1. Follow the detailed guide in `GOOGLE_OAUTH_SETUP.md`
2. Get your Google OAuth credentials from Google Cloud Console
3. Update the `.env` file in `fastapi-backend/` folder
4. Restart the FastAPI server

**Without Google OAuth:** The app will work fine with just the local authentication (testuser/testpass123)

**With Google OAuth:** Users can log in with their Google accounts

## Quick Start

### 2. Start the FastAPI Backend (Terminal 1)

```bash
cd fastapi-backend
# Activate virtual environment (already configured)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Backend will be available at:** http://localhost:8000

### 3. Start the React Frontend (Terminal 2)

```bash
cd my-react-app
npm start
```

**Frontend will be available at:** http://localhost:3000

## API Endpoints

### FastAPI Backend (Port 8000)

- `GET /` - Root endpoint with OAuth status
- `GET /auth/google` - Initiate Google OAuth login
- `GET /auth/google/callback` - Google OAuth callback handler
- `GET /auth/google/url` - Get Google OAuth URL for frontend
- `POST /api/login` - User login (sets session cookie)
- `POST /api/logout` - User logout (clears session cookie)
- `GET /api/me` - Get current user info (requires authentication)
- `GET /api/hello` - Hello World API (personalized if authenticated)
- `GET /api/status` - Backend status with authentication info
- `GET /api/sessions` - View active sessions (requires authentication)
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation

### Authentication Options

**1. Google OAuth (Recommended):**
- Click "Sign in with Google" button
- Secure OAuth 2.0 flow
- No password required

**2. Local Account:**
- Username: `testuser`
- Password: `testpass123`

### Testing the Integration

1. Open http://localhost:3000 in your browser
2. Click "Get Hello from FastAPI" button
3. You should see a successful response from the backend

## Current Status

✅ **Backend (FastAPI)**: Running on http://localhost:8000
✅ **Frontend (React)**: Running on http://localhost:3000
✅ **CORS**: Configured for localhost:3000 with credentials
✅ **API Integration**: React can successfully call FastAPI endpoints
✅ **Cookie Authentication**: JWT-based session management
✅ **Secure Cookies**: HTTP-only, SameSite protection
✅ **Session Management**: Login/logout with persistent sessions
✅ **Google OAuth**: OAuth 2.0 integration ready (needs credentials)

## Authentication Features

### 🍪 Cookie-Based Authentication
- **JWT Tokens**: Secure session tokens with expiration
- **HTTP-Only Cookies**: Prevents XSS attacks
- **SameSite Protection**: CSRF protection
- **Session Storage**: In-memory session tracking (use Redis in production)
- **Automatic Expiration**: 24-hour session timeout
- **Secure Headers**: CORS with credentials enabled

### 🔍 Google OAuth 2.0 Integration
- **OAuth Flow**: Complete OAuth 2.0 implementation
- **User Profile**: Automatic user creation from Google profile
- **Secure Redirect**: Proper callback handling
- **Multi-Provider**: Supports both local and Google authentication
- **Session Unification**: Same session system for all auth methods

### 🌐 Frontend Integration
- **Automatic Cookie Management**: Browser handles cookie storage
- **Dual Login Options**: Traditional form + Google OAuth button
- **Authentication State**: Persistent login state across page reloads
- **Session Monitoring**: View active sessions and user info
- **Logout Functionality**: Properly clears session cookies

## Next Features to Implement

- ✅ Authentication & Authorization (JWT)
- ✅ Cookie management with secure session handling
- � Database integration (PostgreSQL/SQLite)
- 👤 User registration system
- 🛡️ Protected routes and role-based access
- 🔐 Password hashing with bcrypt
- 📱 Responsive design
- 🧪 Unit and integration tests
- 🔄 Password reset functionality
- 👥 User profile management

## Development

- **Frontend Hot Reload**: Enabled (React will auto-refresh on changes)
- **Backend Hot Reload**: Enabled (FastAPI will auto-reload on changes)
- **API Documentation**: Visit http://localhost:8000/docs for interactive API docs

## Troubleshooting

If you encounter CORS errors:
1. Make sure both servers are running
2. Check that FastAPI is running on port 8000
3. Check that React is running on port 3000
4. Verify CORS settings in `fastapi-backend/main.py`