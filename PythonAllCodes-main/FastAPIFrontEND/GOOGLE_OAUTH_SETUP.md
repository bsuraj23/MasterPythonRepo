# Google OAuth Setup Guide

Follow these steps to configure Google OAuth for your FastAPI + React application.

## 1. Create Google OAuth Credentials

### Step 1: Go to Google Cloud Console
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account

### Step 2: Create or Select a Project
1. Click on the project dropdown at the top
2. Either select an existing project or click "New Project"
3. Give your project a name (e.g., "FastAPI React OAuth")
4. Click "Create"

### Step 3: Enable Required APIs
1. Go to "APIs & Services" > "Library"
2. Search for and enable:
   - **Google+ API** (for user profile info)
   - **Google OAuth2 API** (for authentication)

### Step 4: Create OAuth 2.0 Credentials
1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth 2.0 Client IDs"
3. If prompted, configure the OAuth consent screen first:
   - Choose "External" for user type
   - Fill in required fields (App name, User support email, etc.)
   - Add your email to test users
4. For Application type, select "Web application"
5. Give it a name (e.g., "FastAPI React App")

### Step 5: Configure Redirect URIs
Add these URIs to your OAuth client:

**Authorized JavaScript origins:**
```
http://localhost:3000
```

**Authorized redirect URIs:**
```
http://localhost:8000/auth/google/callback
```

### Step 6: Get Your Credentials
After creating, you'll see:
- **Client ID** (looks like: 123456789-abcdefg.apps.googleusercontent.com)
- **Client Secret** (looks like: GOCSPX-xxxxxxxxxxxxxxxxxxxxxxxx)

## 2. Configure Your Application

### Update .env file
Edit `fastapi-backend/.env` and replace the placeholder values:

```env
# Google OAuth Configuration
GOOGLE_CLIENT_ID=your_actual_client_id_here
GOOGLE_CLIENT_SECRET=your_actual_client_secret_here
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback

# Application settings
SECRET_KEY=your-secret-key-change-this-in-production
FRONTEND_URL=http://localhost:3000
```

### Restart the FastAPI Server
After updating the .env file, restart your FastAPI server to load the new configuration.

## 3. Test Google OAuth

1. Start both servers (React on :3000, FastAPI on :8000)
2. Open http://localhost:3000
3. You should see a "Sign in with Google" button
4. Click it to test the OAuth flow

## 4. OAuth Flow Explanation

1. **User clicks "Sign in with Google"** → Redirects to Google OAuth
2. **User authorizes your app** → Google redirects back to your callback
3. **FastAPI receives authorization code** → Exchanges it for access token
4. **FastAPI gets user info** → Creates session and sets cookie
5. **User redirected to React app** → Now logged in with Google account

## 5. Security Notes

- Keep your Client Secret secure and never commit it to version control
- In production, use HTTPS and set `secure=True` for cookies
- Consider implementing additional security measures like CSRF tokens
- Regularly rotate your OAuth credentials

## 6. Troubleshooting

### Common Issues:

**"OAuth client not found" error:**
- Check that your Client ID is correct in the .env file
- Ensure the project is selected correctly in Google Cloud Console

**"Redirect URI mismatch" error:**
- Verify the redirect URI in Google Cloud Console matches exactly
- Make sure there are no extra spaces or characters

**"Access blocked" error:**
- Add your email to test users in the OAuth consent screen
- Ensure your app is not restricted to internal users only

**Cookie not being set:**
- Check that CORS is configured with `credentials: true`
- Verify the frontend URL matches the one in CORS settings

## 7. Production Deployment

When deploying to production:

1. Update redirect URIs to use your production domain
2. Set `secure=True` for cookies (requires HTTPS)
3. Use environment variables for all sensitive configuration
4. Consider using a proper session store (Redis, database) instead of in-memory storage

## Success! 🎉

Once configured correctly, users can log in with their Google accounts and enjoy a seamless authentication experience across your React + FastAPI application.