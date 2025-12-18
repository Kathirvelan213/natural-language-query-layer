from fastapi import APIRouter
from .health_router import router as health_router
from .query_router import router as query_router

router = APIRouter()

router.include_router(health_router)
router.include_router(query_router)