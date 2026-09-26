from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import analysis, documents, health, knowledge, auth, citations, workspace, system, exports

app = FastAPI(
    title="AYURLEX Intelligence Engine",
    description="Multilingual API for Ayurvedic Intelligence and Innovation",
    version="1.0.0"
)

# Configure CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to actual frontend domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(health.router, tags=["Health"])
app.include_router(analysis.router, tags=["Analysis"], prefix="/analysis")
app.include_router(documents.router, tags=["Documents"], prefix="/documents")
app.include_router(knowledge.router, tags=["Knowledge"])
app.include_router(auth.router, tags=["Auth"], prefix="/auth")
app.include_router(citations.router, tags=["Citations"], prefix="/citations")
app.include_router(workspace.router, tags=["Workspace"], prefix="/workspace")
app.include_router(system.router, tags=["System Services"], prefix="/system")
app.include_router(exports.router, tags=["Exports"], prefix="/exports")
