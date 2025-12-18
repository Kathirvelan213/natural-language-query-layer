from fastapi import FastAPI
from API.routers import router as api_router

app=FastAPI(title="Natural Language Query Layer API",version="1.0.0")
app.include_router(api_router,prefix="/api")
