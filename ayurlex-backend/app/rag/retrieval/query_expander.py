from typing import List
from app.rag.models import RAGQueryRequest

class QueryExpander:
    """
    Expands the query using relevant AYURLEX terminology (scientific names, aliases).
    """
    def expand(self, request: RAGQueryRequest) -> List[str]:
        expanded_terms = set([request.query])
        
        # Add basic ingredients
        if request.ingredients:
            for ing in request.ingredients:
                expanded_terms.add(ing)
                
        # Add normalized and scientific terms
        if request.normalized_terms:
            for norm in request.normalized_terms:
                if norm.user_input:
                    expanded_terms.add(norm.user_input)
                if norm.normalized:
                    expanded_terms.add(norm.normalized)
                if getattr(norm, 'scientific', None):
                    expanded_terms.add(norm.scientific)
                if getattr(norm, 'english', None):
                    expanded_terms.add(norm.english)
                    
        # Add context-specific expansion
        if request.module == "formulation_analysis":
            expanded_terms.update(["formulation", "preparation", "combination"])
            
        return list(set(filter(None, expanded_terms)))

query_expander = QueryExpander()
