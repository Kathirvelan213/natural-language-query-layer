from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from api.routers import router as api_router
from api.routers.auth_router import router as auth_router
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import os
import time

from dotenv import load_dotenv
load_dotenv()

app=FastAPI(title="Natural Language Query Layer API",version="1.0.0")

# Get allowed origins from environment or use default
allowed_origins = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom middleware to expire anonymous sessions
class AnonymousSessionExpiryMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Check if session exists and is anonymous
        if "user_id" in request.session:
            is_authenticated = request.session.get("is_authenticated", False)
            created_at = request.session.get("created_at")
            
            # Only expire anonymous sessions
            if not is_authenticated and created_at:
                session_ttl = int(os.getenv("SESSION_TTL", "86400"))
                if time.time() - created_at > session_ttl:
                    # Session expired, clear it
                    request.session.clear()
        
        response = await call_next(request)
        return response

app.add_middleware(AnonymousSessionExpiryMiddleware)

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY", "super-secret-key"),
    same_site="lax",
    https_only=False,
    max_age=2592000,  # 30 days for authenticated sessions
)
app.include_router(api_router, prefix="/api")
app.include_router(auth_router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "NL2SQL backend running"}