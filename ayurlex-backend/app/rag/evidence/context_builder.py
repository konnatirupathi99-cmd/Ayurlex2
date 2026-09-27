from typing import List, Dict, Any
from app.rag.models import RAGSystemOutput, QueryAnalysis, RetrievalContext, RetrievalConfidence
from app.models.evidence import RetrievedEvidence

class ContextBuilder:
    """
    Assembles final RAG context package.
    """
    def build(self, 
              analysis_id: str, 
              query_analysis: Dict[str, Any], 
              expanded_terms: List[str],
              evidence: List[RetrievedEvidence], 
              limitations: List[str]) -> RAGSystemOutput:
        
        # Calculate retrieval confidence based on evidence quality
        score = 0.0
        level = "low"
        explanation = "Limited relevant results retrieved."
        
        if evidence:
            avg_relevance = sum(e.relevance_score for e in evidence) / len(evidence)
            score = min(1.0, avg_relevance + (len(evidence) * 0.05))
            
            if score > 0.7:
                level = "high"
                explanation = "Strong relevant evidence found across multiple sources."
            elif score > 0.4:
                level = "moderate"
                explanation = "Some relevant evidence found, but coverage may be limited."
        
        confidence = RetrievalConfidence(
            score=score,
            level=level,
            explanation=explanation
        )
        
        qa = QueryAnalysis(
            original_query=query_analysis.get("main_topic", ""),
            normalized_query=query_analysis.get("main_topic", ""),
            detected_language=query_analysis.get("detected_language", "en"),
            expanded_terms=expanded_terms
        )
        
        ctx = RetrievalContext(
            module=query_analysis.get("module", "general"),
            primary_jurisdiction=query_analysis.get("jurisdiction", "International"),
            secondary_jurisdictions=[]
        )
        
        status = "retrieval_completed"
        if not evidence:
            status = "no_relevant_results"
        elif level == "low":
            status = "limited_results"
            
        retrieved_chunks = [e.content for e in evidence]
        source_metadata = [{"document_id": e.document_id, "category": e.category, "jurisdiction": e.jurisdiction} for e in evidence]
        relevance_scores = [e.relevance_score for e in evidence]
        citation_information = [{"title": e.source_title, "section": e.section or "N/A", "page": str(e.page_number) or "N/A"} for e in evidence]
            
        return RAGSystemOutput(
            analysis_id=analysis_id,
            status=status,
            query_analysis=qa,
            retrieval_context=ctx,
            evidence=evidence,
            retrieved_chunks=retrieved_chunks,
            source_metadata=source_metadata,
            relevance_scores=relevance_scores,
            citation_information=citation_information,
            retrieval_limitations=list(set(limitations)),
            retrieval_confidence=confidence,
            limitations=list(set(limitations)),
            metadata={"total_results": len(evidence), "retrieval_methods": ["hybrid"]}
        )

context_builder = ContextBuilder()
