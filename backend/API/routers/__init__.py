from fastapi import APIRouter
from .query_router import router as query_router
from .chat_router import router as chat_router

router = APIRouter()

router.include_router(query_router)
router.include_router(chat_router, prefix='/chats')

