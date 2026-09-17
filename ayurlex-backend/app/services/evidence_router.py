from typing import List, Dict
from app.models.evidence import RetrievedEvidence

class EvidenceRouter:
    @staticmethod
    def route(evidence: List[RetrievedEvidence]) -> Dict[str, List[RetrievedEvidence]]:
        """
        Routes evidence to the appropriate intelligence modules based on metadata categories.
        Ensures modules only receive relevant context to reduce hallucination and processing overhead.
        """
        routed_evidence = {
            "formulation": [],
            "ip": [],
            "traditional_knowledge": [],
            "abs": [],
            "regulatory": []
        }
        
        for item in evidence:
            cat = item.category.lower()
            if "ip" in cat or "patent" in cat:
                routed_evidence["ip"].append(item)
            elif "tk" in cat or "traditional" in cat:
                routed_evidence["traditional_knowledge"].append(item)
            elif "abs" in cat or "biodiversity" in cat:
                routed_evidence["abs"].append(item)
            elif "regulatory" in cat or "fda" in cat or "ayush" in cat:
                routed_evidence["regulatory"].append(item)
            else:
                # Default to formulation/general context if category is ambiguous
                routed_evidence["formulation"].append(item)
                
        return routed_evidence
