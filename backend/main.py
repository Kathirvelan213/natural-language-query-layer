from fastapi import FastAPI
from api.routers import query_router as api_router
from starlette.middleware.sessions import SessionMiddleware


from dotenv import load_dotenv
load_dotenv()

app=FastAPI(title="Natural Language Query Layer API",version="1.0.0")

app.add_middleware(
    SessionMiddleware,
    secret_key="super-secret-key",  # move to env var in real app
)
app.include_router(api_router,prefix="/api")

@app.get("/")
def root():
    return {"message": "NL2SQL backend running"}