from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import router as api_router
from api.routers.auth_router import router as auth_router
from starlette.middleware.sessions import SessionMiddleware
import os

from dotenv import load_dotenv
load_dotenv()

app=FastAPI(title="Natural Language Query Layer API",version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY", "super-secret-key"),
)
app.include_router(api_router, prefix="/api")
app.include_router(auth_router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "NL2SQL backend running"}