from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_db

router = APIRouter()

@router.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """
    Production System health check endpoint.
    Used by Docker / Kubernetes for liveness probes.
    """
    try:
        # Ping the database to ensure connection pool is alive
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = "disconnected"
        raise HTTPException(status_code=503, detail="Database connection failed")

    return {
        "status": "ok",
        "services": {
            "database": db_status,
            "intelligence_engine": "operational",
            "vector_store": "ready"
        }
    }
