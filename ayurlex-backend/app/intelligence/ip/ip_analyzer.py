from typing import List
from app.models.intelligence_input import IntelligenceInput
from app.models.evidence import RetrievedEvidence
from app.models.intelligence_output import IPModuleOutput, PatentContextOutput, ConfidenceIndicator

from app.intelligence.ip.evidence_evaluator import IPEvidenceEvaluator
from app.intelligence.ip.prior_art_analyzer import PriorArtAnalyzer
from app.intelligence.ip.similarity_engine import IPSimilarityEngine
from app.intelligence.ip.differentiation_analyzer import DifferentiationAnalyzer
from app.intelligence.ip.trademark_context import TrademarkContextAnalyzer
from app.intelligence.ip.confidence_calculator import IPConfidenceCalculator

async def analyze_ip(input_data: IntelligenceInput, evidence: List[RetrievedEvidence]) -> IPModuleOutput:
    """
    IP Intelligence Engine Orchestrator
    """
    jurisdiction = input_data.jurisdiction or "India"
    
    # MOCK FOR PROTOTYPE:
    # If the user tests this, we want to inject a mock IP evidence so they can see the full differentiation
    # engine run, because otherwise RAG returns empty right now.
    if input_data.innovation_name == "Test" and not evidence:
        import uuid
        evidence.append(RetrievedEvidence(
            evidence_id=f"EV-{str(uuid.uuid4())[:8].upper()}",
            source_id="MOCK-IN2021000",
            content="Herbal formulation patent for immunity containing Withania somnifera and Curcuma longa.",
            category="Patent",
            relevance_score=0.85,
            title="Mock Patent Application: IN2021000",
            language="en",
            jurisdiction=jurisdiction
        ))
    
    # 1. Evaluate Evidence strictly for IP context
    ip_evidence = IPEvidenceEvaluator.evaluate(evidence, jurisdiction)
    
    # 2. Run independent sub-analyzers
    patent_context_data = IPSimilarityEngine.analyze(input_data, ip_evidence)
    prior_art_output = PriorArtAnalyzer.analyze(input_data, ip_evidence)
    differentiation_output = DifferentiationAnalyzer.analyze(input_data, ip_evidence)
    trademark_output = TrademarkContextAnalyzer.analyze(input_data)
    
    # 3. Calculate Confidence
    confidence_data = IPConfidenceCalculator.calculate(input_data, ip_evidence)
    
    # 4. Synthesize Status and Actions
    status = "completed"
    summary = ""
    recommended_actions = []
    key_findings = []
    
    if not ip_evidence:
        status = "Limited Evidence"
        summary = "IP Intelligence analysis completed with limited evidence. Findings are advisory."
        recommended_actions.append("Conduct a detailed jurisdiction-specific prior-art review.")
        key_findings.append("No direct prior-art matches found in current retrieval.")
    else:
        summary = f"IP Intelligence analysis completed for {jurisdiction}. Relevant references identified."
        recommended_actions.append("Review potentially similar technical references.")
        recommended_actions.append("Document differentiating technical features.")
        key_findings.append("Potential similarity identified in retrieved references.")
        
    recommended_actions.append("Seek specialist IP advice where required.")
    
    return IPModuleOutput(
        module="ip_intelligence",
        status=status,
        summary=summary,
        patent_context=PatentContextOutput(**patent_context_data),
        prior_art=prior_art_output,
        innovation_differentiation=differentiation_output,
        trademark_context=trademark_output,
        key_findings=key_findings,
        supporting_evidence=evidence, # return original for API
        confidence=confidence_data["score"],
        limitations=confidence_data["limitations"],
        recommended_actions=recommended_actions
    )
