import re
from typing import List, Dict, Any
from app.rag.models import RAGQueryRequest

class QueryAnalyzer:
    """
    Analyzes the user query before retrieval.
    Extracts main topic, ingredients, and context.
    """
    def analyze(self, request: RAGQueryRequest) -> Dict[str, Any]:
        analysis = {
            "main_topic": request.query,
            "ingredients": request.ingredients or [],
            "module": request.module,
            "product_type": "Unknown",
            "jurisdiction": request.jurisdiction,
            "detected_language": request.detected_language
        }
        
        # Simple heuristic extraction if not provided
        lower_query = request.query.lower()
        if "wellness" in lower_query or "supplement" in lower_query:
            analysis["product_type"] = "Wellness Product"
        elif "cosmetic" in lower_query:
            analysis["product_type"] = "Cosmetic"
            
        return analysis

query_analyzer = QueryAnalyzer()
