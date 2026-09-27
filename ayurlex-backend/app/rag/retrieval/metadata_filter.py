from typing import Dict, Any
from app.rag.models import RAGQueryRequest

class MetadataFilter:
    """
    Builds filters for restricting evidence retrieval based on jurisdiction, category, etc.
    """
    def build_filters(self, request: RAGQueryRequest) -> Dict[str, Any]:
        filters = {}
        
        # Primary jurisdiction filter
        if request.jurisdiction and request.jurisdiction.lower() != "international":
            filters["jurisdiction"] = request.jurisdiction
            
        if request.detected_language:
            filters["language"] = request.detected_language
            
        if request.filters:
            # Handle additional explicit filters like date, category, etc.
            for key, value in request.filters.items():
                if key in ["category", "publication_date", "effective_date"]:
                    filters[key] = value
                    
        return filters

metadata_filter = MetadataFilter()
