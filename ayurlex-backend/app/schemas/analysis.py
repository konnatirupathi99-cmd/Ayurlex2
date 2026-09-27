from pydantic import BaseModel
from typing import Optional

class AnalysisRequest(BaseModel):
    query: str
    context: Optional[dict] = None
    type: str = "general" # Can be 'ip', 'regulatory', 'formulation'
