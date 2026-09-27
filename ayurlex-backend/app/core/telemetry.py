import logging
import json
import uuid
from datetime import datetime, timezone
from contextvars import ContextVar
from typing import Any, Dict, Optional

# Context variables for tracing
request_id_ctx: ContextVar[str] = ContextVar("request_id", default="system")
user_id_ctx: ContextVar[str] = ContextVar("user_id", default="anonymous")
session_id_ctx: ContextVar[str] = ContextVar("session_id", default="unknown")

class StructuredJSONFormatter(logging.Formatter):
    """Formats logs strictly into structured JSON for observability platforms."""
    def format(self, record: logging.LogRecord) -> str:
        # Avoid logging raw sensitive data
        log_record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "request_id": request_id_ctx.get(),
            "user_id": user_id_ctx.get(),
            "session_id": session_id_ctx.get(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage()
        }

        # If a dictionary is passed in `extra`, merge it safely
        if hasattr(record, "telemetry"):
            telemetry_data = getattr(record, "telemetry")
            if isinstance(telemetry_data, dict):
                # Clean sensitive keys natively
                sensitive_keys = {"password", "token", "api_key", "secret", "hashed_password"}
                clean_telemetry = {
                    k: v for k, v in telemetry_data.items() 
                    if k.lower() not in sensitive_keys
                }
                log_record.update(clean_telemetry)

        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_record)

def setup_telemetry():
    logger = logging.getLogger("ayurlex")
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(StructuredJSONFormatter())
        logger.addHandler(handler)
        
    return logger

ayurlex_logger = setup_telemetry()

def track_event(module: str, event_type: str, status: str, latency_ms: Optional[float] = None, error: Optional[str] = None, **kwargs):
    """
    Centralized telemetry tracking helper.
    """
    telemetry_data = {
        "module": module,
        "event_type": event_type,
        "status": status,
    }
    if latency_ms is not None:
        telemetry_data["latency_ms"] = round(latency_ms, 2)
    if error is not None:
        telemetry_data["error_information"] = error
        
    telemetry_data.update(kwargs)
    
    log_level = logging.ERROR if status == "error" else logging.INFO
    ayurlex_logger.log(log_level, f"[{module}] {event_type}", extra={"telemetry": telemetry_data})
