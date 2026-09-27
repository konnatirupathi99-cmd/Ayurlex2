import re
from typing import List, Dict, Any
from app.ai.safety.models import ResponseValidationResult, ConfidenceLabel
from app.ai.safety.evidence_evaluator import EvidenceEvaluation

class ResponseValidator:
    
    def __init__(self):
        # Patterns that indicate false claims of certainty or unsupported conclusions
        self.risk_patterns = [
            r"(?i)this is definitively approved by cdsco", # Must be backed by evidence
            r"(?i)this patent is valid", # AI shouldn't make legal claims
            r"(?i)it is absolutely guaranteed",
            r"(?i)100% cure"
        ]

    def validate_generation(
        self, 
        generated_text: str, 
        evidence_eval: EvidenceEvaluation,
        retrieved_evidence: List[Dict[str, Any]]
    ) -> ResponseValidationResult:
        """
        Validates the generated AI response.
        Rejects/revises responses with fabricated sources, unsupported conclusions, false claims.
        """
        warnings = []
        is_valid = True
        rejection_reason = None
        revised = generated_text
        
        # 1. Check for false claims of certainty / unsupported legal conclusions
        for pattern in self.risk_patterns:
            if re.search(pattern, generated_text):
                is_valid = False
                rejection_reason = "Unsupported legal conclusion or false claim of certainty detected."
                break
                
        # 2. Check for fabricated citations
        # If the LLM generates a citation like [Source: X] but X is not in retrieved_evidence
        citations_in_text = re.findall(r"\[Source:\s*(.*?)\]", generated_text)
        actual_sources = [e.get("source", "") for e in retrieved_evidence]
        
        for cit in citations_in_text:
            # Simple substring match check
            if not any(cit.lower() in src.lower() for src in actual_sources if src):
                is_valid = False
                rejection_reason = f"Fabricated source detected: {cit}"
                break
                
        # 3. Explicitly state when authoritative evidence was unavailable
        if evidence_eval.confidence_label == ConfidenceLabel.INSUFFICIENT:
            if "authoritative evidence" not in generated_text.lower():
                revised = "Note: Authoritative evidence was unavailable for this query.\n\n" + revised
                
        # 4. Attach the confidence label textually if needed, or pass it in struct
        return ResponseValidationResult(
            is_valid=is_valid,
            rejection_reason=rejection_reason,
            confidence_label=evidence_eval.confidence_label,
            warnings=warnings,
            revised_response=revised if is_valid else None
        )

response_validator = ResponseValidator()
