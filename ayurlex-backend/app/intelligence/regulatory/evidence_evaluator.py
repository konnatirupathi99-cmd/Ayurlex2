from typing import List, Dict, Any
from app.models.evidence import RetrievedEvidence

class EvidenceEvaluator:
    def analyze(self, evidence: List[RetrievedEvidence], jurisdiction: str) -> Dict[str, Any]:
        valid_evidence = []
        signals = []
        
        for e in evidence:
            if not e.evidence_id or not e.content:
                continue
                
            if jurisdiction and jurisdiction.lower() != "international" and e.jurisdiction:
                if jurisdiction.lower() not in e.jurisdiction.lower() and e.jurisdiction.lower() != "international":
                    continue
                    
            if not any(v.evidence_id == e.evidence_id for v in valid_evidence):
                valid_evidence.append(e)
                
        if not valid_evidence:
            signals.append("LIMITED REGULATORY EVIDENCE AVAILABLE")
        else:
            signals.append("RELEVANT REGULATORY INFORMATION RETRIEVED")
            
        return {
            "status": "completed",
            "signals": signals,
            "valid_evidence": valid_evidence
        }
