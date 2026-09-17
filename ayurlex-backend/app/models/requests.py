from pydantic import BaseModel
from typing import List, Optional

class AnalysisRequest(BaseModel):
    innovation_name: str
    query: str
    product_type: str
    ingredients: List[str]
    jurisdiction: str
    language: str
    output_language: str
