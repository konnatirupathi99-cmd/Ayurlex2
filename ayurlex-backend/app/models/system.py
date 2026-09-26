from pydantic import BaseModel
from typing import List

class SystemHealth(BaseModel):
    status: str
    database: str
    external_citation_service: str

class RuntimeConfig(BaseModel):
    citation_limit: int
    request_timeout_seconds: int
    supported_languages: List[str]
    default_jurisdiction: str
    preview_behavior: str
