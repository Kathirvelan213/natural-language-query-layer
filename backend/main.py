from fastapi import FastAPI
from api.routers import query_router as api_router

from dotenv import load_dotenv
load_dotenv()

app=FastAPI(title="Natural Language Query Layer API",version="1.0.0")
app.include_router(api_router,prefix="/api")

@app.get("/")
def root():
    return {"message": "NL2SQL backend running"}