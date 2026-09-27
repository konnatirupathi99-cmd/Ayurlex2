from fastapi import APIRouter

from app.api.endpoints import (
    auth,
    users,
    chat,
    analysis,
    documents,
    knowledge,
    memory,
    history,
    sources,
    feedback,
    health,
    multilingual,
    search
)

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(search.router)
api_router.include_router(chat.router, tags=["chat"])
api_router.include_router(analysis.router, tags=["analysis"])
api_router.include_router(documents.router, tags=["documents"])
api_router.include_router(knowledge.router, tags=["knowledge"])
api_router.include_router(memory.router, tags=["memory"])
api_router.include_router(multilingual.router, tags=["multilingual"])
api_router.include_router(history.router, tags=["history"])
api_router.include_router(sources.router, tags=["sources"])
api_router.include_router(feedback.router, tags=["feedback"])
api_router.include_router(health.router, tags=["system"])
