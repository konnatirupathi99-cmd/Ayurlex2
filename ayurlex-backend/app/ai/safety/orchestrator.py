from typing import List, Dict, Any, Tuple
from app.ai.safety.models import SafetyCheckResult, EvidenceEvaluation, ResponseValidationResult
from app.ai.safety.prompt_shield import prompt_shield
from app.ai.safety.evidence_evaluator import evidence_evaluator
from app.ai.safety.response_validator import response_validator

class SafetyOrchestrator:
    """
    Main AYURLEX AI safety and evidence-control layer.
    """
    
    def pre_generation_check(self, query: str) -> SafetyCheckResult:
        """
        Step 1: Validate the query for prompt injection or restricted commands.
        """
        return prompt_shield.sanitize_user_query(query)
        
    def prepare_evidence(self, query: str, retrieved_evidence: List[Dict[str, Any]]) -> Tuple[EvidenceEvaluation, List[str]]:
        """
        Step 2: Evaluate retrieved evidence, calculate confidence, identify gaps.
        Step 3: Format the documents safely as data, not instructions.
        """
        evaluation = evidence_evaluator.evaluate(query, retrieved_evidence)
        
        safe_documents = []
        for ev in retrieved_evidence:
            content = ev.get("content", "")
            safe_doc = prompt_shield.format_document_as_data(content)
            safe_documents.append(safe_doc)
            
        return evaluation, safe_documents

    def post_generation_check(
        self, 
        generated_text: str, 
        evaluation: EvidenceEvaluation,
        retrieved_evidence: List[Dict[str, Any]]
    ) -> ResponseValidationResult:
        """
        Step 4: Validate the AI's response against fabricated citations and unsupported claims.
        Revises the text if necessary (e.g. adding insufficient evidence warnings).
        """
        return response_validator.validate_generation(generated_text, evaluation, retrieved_evidence)

safety_orchestrator = SafetyOrchestrator()
