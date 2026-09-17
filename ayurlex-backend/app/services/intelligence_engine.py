import uuid
from typing import List, Dict, Any

from app.models.requests import AnalysisRequest
from app.models.responses import IntelligenceReport as APIResponseReport

# Import Intelligence Core Models
from app.models.intelligence_input import IntelligenceInput
from app.models.evidence import RetrievedEvidence
from app.models.intelligence_output import CoreIntelligenceOutput, ModuleOutput

# Import Services
from app.services.language_service import detect_language
from app.services.terminology_service import normalize_terms
from app.rag.retrieval import retrieve_evidence
from app.services.evidence_router import EvidenceRouter

# Import Intelligence Modules
from app.intelligence.formulation.formulation_analyzer import analyze_formulation
from app.intelligence.ip.ip_analyzer import analyze_ip
from app.intelligence.traditional_knowledge.tk_analyzer import analyze_traditional_knowledge
from app.intelligence.abs.abs_analyzer import analyze_abs
from app.intelligence.regulatory import analyze_regulatory

# Import Engines
from app.intelligence.signal_aggregator import SignalAggregator
from app.intelligence.confidence_engine import ConfidenceEngine
from app.intelligence.limitation_detector import LimitationDetector

async def process_analysis(request: AnalysisRequest) -> CoreIntelligenceOutput:
    """
    14-Step Core Intelligence Orchestration Flow
    """
    analysis_id = f"AYR-{uuid.uuid4().hex[:6].upper()}"
    
    # 1. Validate Input (Pydantic validates structure, we just extract here)
    # 2. Validate Normalized Language Data
    detected_lang = detect_language(request.query, request.ingredients)
    
    # 3. Validate Ayurvedic Term Mapping
    normalized_terms = normalize_terms(request.ingredients)
    
    # 4. Retrieve Evidence
    # Mocking RetrievedEvidence objects since retrieval.py just returns empty list currently
    raw_evidence = []
    
    # Construct Intelligence Input
    intelligence_input = IntelligenceInput(
        analysis_id=analysis_id,
        innovation_name=request.innovation_name,
        innovation_description=request.query,
        product_type=request.product_type,
        ingredients=request.ingredients,
        normalized_ingredients=normalized_terms,
        jurisdiction=request.jurisdiction,
        detected_language=detected_lang,
        output_language=request.output_language,
        retrieved_evidence=raw_evidence
    )
    
    # 5. Classify Evidence
    routed_evidence = EvidenceRouter.route(intelligence_input.retrieved_evidence)
    
    # 6-10. Run Intelligence Modules (Awaiting all concurrently is ideal, running sequentially here for simplicity)
    formulation_mod = await analyze_formulation(intelligence_input, routed_evidence["formulation"])
    ip_mod = await analyze_ip(intelligence_input, routed_evidence["ip"])
    tk_mod = analyze_traditional_knowledge(intelligence_input, routed_evidence["traditional_knowledge"])
    abs_mod = await analyze_abs(intelligence_input, routed_evidence["abs"])
    regulatory_mod = await analyze_regulatory(intelligence_input, routed_evidence["regulatory"])
    
    modules = {
        "formulation": formulation_mod,
        "ip": ip_mod,
        "traditional_knowledge": tk_mod,
        "abs": abs_mod,
        "regulatory": regulatory_mod
    }
    
    # 11. Aggregate Signals
    key_findings = SignalAggregator.aggregate(modules)
    
    # 12. Calculate Confidence
    input_completeness = 1.0 if (request.ingredients and request.jurisdiction and request.query) else 0.5
    confidence = ConfidenceEngine.calculate(modules, len(raw_evidence), input_completeness)
    
    # 13. Identify Limitations
    limitations = LimitationDetector.detect(intelligence_input, modules)
    
    # Next steps aggregation
    recommended_next_steps = []
    for mod in modules.values():
        recommended_next_steps.extend(mod.recommended_actions)
        
    # 14. Generate Structured Intelligence Output
    return CoreIntelligenceOutput(
        analysis_id=analysis_id,
        status="completed",
        processing={
            "language_detected": detected_lang,
            "evidence_count": str(len(raw_evidence))
        },
        formulation_intelligence=formulation_mod,
        ip_intelligence=ip_mod,
        traditional_knowledge=tk_mod,
        abs_context=abs_mod,
        regulatory_context=regulatory_mod,
        key_findings=key_findings,
        evidence=raw_evidence,
        confidence=confidence,
        limitations=limitations,
        recommended_next_steps=list(set(recommended_next_steps))
    )

async def generate_intelligence_report(request: AnalysisRequest) -> APIResponseReport:
    """
    Bridge function: Runs the core engine, then passes it to AI synthesis.
    """
    from app.services.ai_service import synthesize_report
    
    # Run Core Engine
    core_output = await process_analysis(request)
    
    # Pass to AI Synthesis (which maps CoreOutput to the final APIResponseReport)
    # Note: I'm adjusting synthesize_report signature locally in ai_service in next step to accept CoreIntelligenceOutput
    normalized_terms = normalize_terms(request.ingredients)
    report = await synthesize_report(
        request=request,
        core_output=core_output,
        normalized_terms=normalized_terms
    )
    
    return report
