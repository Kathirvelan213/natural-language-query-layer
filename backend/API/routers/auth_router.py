from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
import os
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request as GoogleRequest
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

router = APIRouter()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/auth/callback")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

SCOPES = ["openid",'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']

@router.get("/login")
async def login(request: Request):
    """Initiate Google OAuth login"""
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [GOOGLE_REDIRECT_URI]
            }
        },
        scopes=SCOPES
    )
    
    flow.redirect_uri = GOOGLE_REDIRECT_URI
    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
    
    request.session['state'] = state
    return RedirectResponse(url=authorization_url)

@router.get("/callback")
async def callback(request: Request, code: str = None, state: str = None):
    """Handle Google OAuth callback"""
    if not code:
        raise HTTPException(status_code=400, detail="Missing authorization code")
    
    session_state = request.session.get('state')
    if not session_state or session_state != state:
        raise HTTPException(status_code=400, detail="State mismatch")
    
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [GOOGLE_REDIRECT_URI]
            }
        },
        scopes=SCOPES,
        state=state
    )
    
    flow.redirect_uri = GOOGLE_REDIRECT_URI
    credentials = flow.fetch_token(code=code)
    
    # Fetch user info from Google
    import requests
    user_info_response = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo',
        headers={'Authorization': f"Bearer {credentials['access_token']}"}
    )
    user_info = user_info_response.json()
    
    # Store user info in session
    request.session['user_id'] = user_info.get('id')
    request.session['email'] = user_info.get('email')
    request.session['name'] = user_info.get('name')
    request.session['picture'] = user_info.get('picture')
    request.session['is_authenticated'] = True
    request.session['credentials'] = {
        'access_token': credentials['access_token'],
        'refresh_token': credentials.get('refresh_token'),
        'token_expiry': credentials.get('expires_in')
    }
    
    # Redirect to frontend with success
    return RedirectResponse(url=FRONTEND_URL)

@router.get("/user")
async def get_user(request: Request):
    """Get current user info"""
    user_id = request.session.get('user_id')
    is_authenticated = request.session.get('is_authenticated', False)
    
    if not user_id or not is_authenticated:
        # Return anonymous user status
        return {
            "is_authenticated": False,
            "user_id": user_id if user_id else None
        }
    
    # Return authenticated user info
    return {
        "is_authenticated": True,
        "user_id": user_id,
        "email": request.session.get('email'),
        "name": request.session.get('name'),
        "picture": request.session.get('picture')
    }

@router.post("/logout")
async def logout(request: Request):
    """Logout user"""
    # Clear existing session
    request.session.clear()
    
    return {
        "message": "Logged out successfully"
    }
    
