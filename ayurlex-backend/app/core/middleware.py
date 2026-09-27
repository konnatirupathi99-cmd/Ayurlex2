import uuid
import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)

class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        from app.core.telemetry import request_id_ctx, track_event
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        request_id_ctx.set(request_id)
        
        start_time = time.time()
        
        try:
            response = await call_next(request)
            
            process_time_ms = (time.time() - start_time) * 1000
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time"] = str(process_time_ms / 1000)
            
            status_category = "success" if response.status_code < 400 else "error"
            track_event(
                module="Application",
                event_type="api_request",
                status=status_category,
                latency_ms=process_time_ms,
                path=request.url.path,
                method=request.method,
                status_code=response.status_code
            )
            return response
            
        except Exception as exc:
            process_time_ms = (time.time() - start_time) * 1000
            track_event(
                module="Application",
                event_type="api_exception",
                status="error",
                latency_ms=process_time_ms,
                path=request.url.path,
                method=request.method,
                error=str(exc)
            )
            raise
