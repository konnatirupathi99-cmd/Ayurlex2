from typing import Dict, Any, List
from app.models.intelligence_input import IntelligenceInput
from app.intelligence.abs.models import ABSEvidenceContext

class ABSJurisdictionContext:
    @staticmethod
    def analyze(input_data: IntelligenceInput, evidence: List[ABSEvidenceContext]) -> Dict[str, Any]:
        """
        Maps user jurisdiction to context signals.
        """
        jurisdiction = (input_data.jurisdiction or "Other / Not Specified").strip()
        signals = []
        
        # Filter evidence relevant to this jurisdiction
        jurisdiction_evidence = [e for e in evidence if e.jurisdiction.lower() == jurisdiction.lower()]
        
        if jurisdiction.lower() == "india":
            signals.append(f"Jurisdiction-Specific Review Recommended for {jurisdiction}")
        elif jurisdiction.lower() == "international":
            signals.append("International ABS Context Review Recommended (Nagoya Protocol)")
        else:
            signals.append("Other / Not Specified Jurisdiction Context")
            
        if not jurisdiction_evidence and jurisdiction.lower() != "other / not specified":
            signals.append("Information Limitations: Limited evidence coverage for the selected jurisdiction")
            
        return {
            "Selected Jurisdiction": jurisdiction,
            "Evidence Jurisdiction": [e.jurisdiction for e in jurisdiction_evidence] if jurisdiction_evidence else ["None"],
            "Context Coverage": "Partial" if jurisdiction_evidence else "Limited",
            "Information Limitations": "Limited evidence coverage" if not jurisdiction_evidence else "None",
            "signals": signals,
            "evidence_ids": [e.evidence_id for e in jurisdiction_evidence]
        }
