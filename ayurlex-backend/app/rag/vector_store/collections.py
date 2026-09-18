class CollectionManager:
    """
    Manages category-based isolation (TK, IP, Regulatory, etc.)
    """
    CATEGORY_TO_COLLECTION = {
        "Traditional Knowledge": "traditional_knowledge",
        "Classical Ayurvedic Knowledge": "traditional_knowledge",
        "Formulation Knowledge": "formulation",
        "Scientific Research": "scientific_research",
        "Patent and IP Context": "ip_intelligence",
        "Regulatory Knowledge": "regulatory",
        "ABS Context": "abs_context",
        "Jurisdiction Knowledge": "jurisdiction",
        "General Reference Material": "general"
    }
    
    MODULE_TO_COLLECTIONS = {
        "traditional_knowledge": ["traditional_knowledge"],
        "formulation_analysis": ["formulation", "traditional_knowledge", "scientific_research"],
        "ip_intelligence": ["ip_intelligence", "scientific_research", "general"],
        "regulatory_intelligence": ["regulatory", "general", "jurisdiction"],
        "abs_context": ["abs_context", "jurisdiction", "traditional_knowledge"],
        "jurisdiction_intelligence": ["jurisdiction", "regulatory", "abs_context"]
    }

    @classmethod
    def get_collection_for_category(cls, category: str) -> str:
        return cls.CATEGORY_TO_COLLECTION.get(category, "general")
        
    @classmethod
    def get_collections_for_module(cls, module: str) -> list[str]:
        return cls.MODULE_TO_COLLECTIONS.get(module, ["general"])
