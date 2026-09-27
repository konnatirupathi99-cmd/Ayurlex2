from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class IntelligenceResult(BaseModel):
    finding: str
    evidence: List[Dict[str, Any]]
    sources: List[str]
    confidence: str
    limitations: List[str]

# Common interface for all intelligence modules
class BaseIntelligenceModule:
    def analyze(self, query: str, context: Dict[str, Any]) -> IntelligenceResult:
        raise NotImplementedError("Subclasses must implement analyze()")
