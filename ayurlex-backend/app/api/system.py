from fastapi import APIRouter, Request, status, HTTPException
from app.models.system import SystemHealth, RuntimeConfig

router = APIRouter()

@router.get("/health", response_model=SystemHealth)
async def system_health():
    """Service health checks for database connectivity and external citation availability."""
    # Mock checks
    return SystemHealth(
        status="ok",
        database="connected",
        external_citation_service="available"
    )

@router.get("/config", response_model=RuntimeConfig)
async def system_config():
    """Runtime configuration for citation limits, request timeouts, supported languages, etc."""
    # Expose only safe status info, no environment variables or secrets
    return RuntimeConfig(
        citation_limit=50,
        request_timeout_seconds=30,
        supported_languages=[
            "en", "hi", "sa", "mr", "ta", "te", "kn", "ml", 
            "bn", "gu", "pa", "or", "ur", "ne", "si", "fr"
        ],
        default_jurisdiction="India (Ayush)",
        preview_behavior="read-only"
    )

class SystemErrors:
    """Centralized error codes."""
    UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
    FORBIDDEN = status.HTTP_403_FORBIDDEN
    VALIDATION = status.HTTP_422_UNPROCESSABLE_ENTITY
    EXTERNAL_SERVICE = status.HTTP_503_SERVICE_UNAVAILABLE
    DATABASE = status.HTTP_500_INTERNAL_SERVER_ERROR
    RATE_LIMIT = status.HTTP_429_TOO_MANY_REQUESTS

def generate_correlation_id() -> str:
    """Request correlation IDs for tracing operations."""
    import uuid
    return f"req-{uuid.uuid4().hex[:8]}"

def log_request(action: str, correlation_id: str, **kwargs):
    """Structured server logging that excludes credentials and raw auth."""
    # Dummy structured logger
    safe_kwargs = {k: v for k, v in kwargs.items() if "token" not in k.lower() and "cookie" not in k.lower()}
    print(f"[CORRELATION:{correlation_id}] ACTION:{action} META:{safe_kwargs}")
