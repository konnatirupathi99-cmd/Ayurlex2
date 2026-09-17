from app.models.requests import AnalysisRequest
from app.models.responses import IntelligenceReport
from app.models.intelligence_output import CoreIntelligenceOutput

async def synthesize_report(
    request: AnalysisRequest, 
    core_output: CoreIntelligenceOutput,
    normalized_terms: list
) -> IntelligenceReport:
    """
    Mock AI Synthesis Layer.
    Translates the structured `CoreIntelligenceOutput` into the final `IntelligenceReport` 
    expected by the frontend, optionally translating the summary based on output language.
    """
    
    # Mock structured response enforcing evidence-first rules
    summary = "Based on available evidence, the formulation combines known botanicals. "
    if core_output.key_findings:
        summary += " ".join(core_output.key_findings[:2]) # Add top 2 findings to summary
        
    if request.output_language == "te":
        summary = "అందుబాటులో ఉన్న ఆధారాల ఆధారంగా, సూత్రీకరణ తెలిసిన వృక్షశాస్త్రాలను మిళితం చేస్తుంది."
    elif request.output_language == "hi":
        summary = "उपलब्ध साक्ष्यों के आधार पर, यह सूत्रीकरण ज्ञात वनस्पतियों को जोड़ता है।"

    return IntelligenceReport(
        analysis_id=core_output.analysis_id,
        innovation_name=request.innovation_name,
        jurisdiction=request.jurisdiction,
        language=request.output_language,
        detected_language=core_output.processing.get("language_detected", "en"),
        summary=summary,
        normalized_terms=normalized_terms,
        formulation_context={
            "classification": core_output.formulation_intelligence.classification.label if core_output.formulation_intelligence.classification else "Unclear",
            "type": core_output.formulation_intelligence.classification.type if core_output.formulation_intelligence.classification else "unclear",
            "details": core_output.formulation_intelligence.classification.summary if core_output.formulation_intelligence.classification else "Pending"
        },
        ip_intelligence={
            "status": core_output.ip_intelligence.status,
            "details": core_output.ip_intelligence.summary,
            "patent_context": core_output.ip_intelligence.patent_context.dict(),
            "prior_art": core_output.ip_intelligence.prior_art.dict(),
            "differentiation": core_output.ip_intelligence.innovation_differentiation.dict(),
            "trademark": core_output.ip_intelligence.trademark_context.dict(),
            "key_findings": core_output.ip_intelligence.key_findings
        },
        traditional_knowledge={
            "status": core_output.traditional_knowledge.status,
            "details": core_output.traditional_knowledge.summary,
            "term_analysis": core_output.traditional_knowledge.term_analysis.dict(),
            "ingredient_analysis": [ia.dict() for ia in core_output.traditional_knowledge.ingredient_analysis],
            "formulation_analysis": core_output.traditional_knowledge.formulation_analysis.dict(),
            "traditional_use_analysis": core_output.traditional_knowledge.traditional_use_analysis.dict(),
            "key_findings": core_output.traditional_knowledge.key_findings
        },
        abs_context={
            "status": core_output.abs_context.signals[0] if core_output.abs_context.signals else "No Signals",
            "details": core_output.abs_context.summary
        },
        regulatory_context={
            "status": core_output.regulatory_context.signals[0] if core_output.regulatory_context.signals else "No Signals",
            "details": core_output.regulatory_context.summary
        },
        evidence=[], # Mock empty evidence mapping
        confidence={
            "score": core_output.confidence.score,
            "level": core_output.confidence.level,
            "limitations": " ".join(core_output.confidence.limitations)
        },
        recommended_next_steps=core_output.recommended_next_steps
    )
