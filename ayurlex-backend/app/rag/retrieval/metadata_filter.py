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
            
        return filters

metadata_filter = MetadataFilter()
