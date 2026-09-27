import logging
from typing import Dict, Any, List

from app.ai.orchestrator_schema import OrchestratorState
from app.ai.safety.orchestrator import safety_orchestrator
from app.multilingual.registry import language_registry
from app.multilingual.terminology import terminology_engine
from app.ai.schema import QueryClassification, EntityExtraction

logger = logging.getLogger(__name__)

class AIOrchestrator:
    """
    Central AYURLEX AI Orchestrator.
    Controls the entire reasoning workflow.
    """
    
    def __init__(self):
        # In a real scenario, these would be initialized service classes
        self.available_modules = [
            "Formulation Analysis", 
            "IP Intelligence", 
            "Traditional Knowledge", 
            "ABS Context", 
            "Regulatory Intelligence", 
            "Jurisdiction Intelligence", 
            "Terminology Engine", 
            "RAG Engine", 
            "Citation Engine"
        ]

    def _classify_query(self, query: str) -> QueryClassification:
        """Mock classification - LLM would decide this based on query"""
        intent = "general"
        if "patent" in query.lower(): intent = "ip_analysis"
        elif "formulation" in query.lower(): intent = "formulation_check"
        elif "cdsco" in query.lower() or "fda" in query.lower(): intent = "regulatory_compliance"
        return QueryClassification(intent=intent, primary_language="en")

    def _detect_jurisdiction(self, query: str) -> str:
        if "india" in query.lower() or "cdsco" in query.lower(): return "India"
        if "usa" in query.lower() or "fda" in query.lower(): return "USA"
        return "International"

    def _plan_modules(self, intent: str) -> List[str]:
        """Decide which modules are relevant instead of executing every module unnecessarily."""
        modules = ["Terminology Engine", "RAG Engine", "Citation Engine"]
        if intent == "ip_analysis": modules.extend(["IP Intelligence", "Traditional Knowledge"])
        elif intent == "formulation_check": modules.extend(["Formulation Analysis", "Traditional Knowledge"])
        elif intent == "regulatory_compliance": modules.extend(["Regulatory Intelligence", "Jurisdiction Intelligence", "ABS Context"])
        return modules

    def _mock_rag_search(self, query: str) -> List[Dict[str, Any]]:
        return [{"source": "Guidelines 2024", "content": "Sample authoritative text."}]

    def execute_workflow(self, query: str, session_context: Dict[str, Any] = None) -> OrchestratorState:
        # 1. Safety Pre-check
        safety_check = safety_orchestrator.pre_generation_check(query)
        if not safety_check.is_safe:
            return OrchestratorState(
                query=query, language="en", jurisdiction="Unknown",
                confidence="Rejected", answer=safety_check.rejection_reason or "Blocked by safety layer."
            )

        # 2. Language Detection
        detected_lang = language_registry.detect_language(query)
        
        # 3. Query Classification
        classification = self._classify_query(query)
        
        # 4. Ayurvedic Term Mapping (Extracting terms would happen here, mocking extraction)
        mock_term = "ashwagandha" if "ashwagandha" in query.lower() else "unknown"
        mapping = terminology_engine.analyze_term(mock_term, detected_lang)
        entities = [mapping.canonical_term] if mapping.canonical_term != "unknown" else []

        # 5. Jurisdiction Detection (Initial)
        jurisdiction = self._detect_jurisdiction(query)
        
        # 6. Retrieval Planning
        modules_to_use = self._plan_modules(classification.intent)
        
        # 7. RAG Search & 8. Specialized Modules
        retrieved_evidence = []
        if "RAG Engine" in modules_to_use:
            retrieved_evidence = self._mock_rag_search(query)
            
        # --- JURISDICTION INTELLIGENCE ---
        from app.intelligence.jurisdiction.jurisdiction_intelligence import jurisdiction_engine
        jurisdiction_analysis = jurisdiction_engine.process_query_jurisdiction(query, retrieved_evidence)
        retrieved_evidence = jurisdiction_analysis.filtered_evidence # Filter out unrelated sources
        
        detected_jurisdictions_str = ", ".join(jurisdiction_analysis.requested_jurisdictions)
        jurisdiction = detected_jurisdictions_str if detected_jurisdictions_str else jurisdiction
            
        # 9. Evidence Aggregation & 10. AI Synthesis Preparation
        evidence_eval, safe_docs = safety_orchestrator.prepare_evidence(query, retrieved_evidence)
        
        # 11. AI Synthesis (Mocking LLM Generation)
        generated_answer = f"Based on the analysis from {', '.join(modules_to_use)}, the findings are... [Source: Guidelines 2024]"
        
        # 12. Citation Validation & 13. Confidence Assessment
        validation = safety_orchestrator.post_generation_check(generated_answer, evidence_eval, retrieved_evidence)
        
        # 14. Final Response
        final_answer = validation.revised_response or generated_answer
        
        if not validation.is_valid:
            final_answer = f"Response Rejected: {validation.rejection_reason}"
            
        from app.ai.citation_engine import citation_engine
        citation_output = citation_engine.format_citations(retrieved_evidence)
        
        # Override the generated answer if no evidence is found
        if not retrieved_evidence:
            final_answer = f"No authoritative evidence was found to support this query in the detected jurisdiction(s) ({detected_jurisdictions_str}). {final_answer}"
            
        # Append Jurisdiction Warnings if any
        if jurisdiction_analysis.jurisdiction_warning:
            final_answer += f"\n\nJURISDICTION WARNING: {jurisdiction_analysis.jurisdiction_warning}\n"
            
        # If there are conflicts, explicitly mention them
        if citation_output.conflicts or jurisdiction_analysis.conflicts_and_limitations:
            conflict_text = "\n\nCONFLICT DETECTED:\n"
            for c in citation_output.conflicts:
                conflict_text += f"- {c.topic}: {c.description} (See citations: {', '.join(c.conflicting_citations)})\n"
            for c in jurisdiction_analysis.conflicts_and_limitations:
                conflict_text += f"- Jurisdiction Note: {c}\n"
            final_answer += conflict_text

        sources_list = [c.source for c in citation_output.citations]

        return OrchestratorState(
            query=query,
            language=detected_lang,
            jurisdiction=jurisdiction,
            entities=entities,
            modules_used=modules_to_use,
            sources=sources_list,
            evidence=[c.dict() for c in citation_output.citations],
            conflicts=[c.description for c in citation_output.conflicts] + evidence_eval.contradictions_detected,
            confidence=validation.confidence_label,
            limitations=evidence_eval.identified_gaps,
            answer=final_answer
        )

    async def stream_workflow(self, query: str, session_context: Dict[str, Any] = None):
        """
        Real-time streaming workflow for AYURLEX.
        Yields structured SSE events.
        """
        import asyncio
        import json

        def _format_sse(event_type: str, data: Any) -> str:
            payload = json.dumps({"event": event_type, "data": data})
            return f"data: {payload}\n\n"

        try:
            # 1. Analyzing query
            yield _format_sse("status", "Analyzing query...")
            await asyncio.sleep(0.5) # Mock processing time
            safety_check = safety_orchestrator.pre_generation_check(query)
            if not safety_check.is_safe:
                yield _format_sse("error", safety_check.rejection_reason or "Blocked by safety layer.")
                yield _format_sse("done", "[DONE]")
                return

            # 2. Detecting language
            yield _format_sse("status", "Detecting language...")
            detected_lang = language_registry.detect_language(query)
            classification = self._classify_query(query)
            await asyncio.sleep(0.5)

            # 3. Mapping terminology
            yield _format_sse("status", "Mapping terminology...")
            mock_term = "ashwagandha" if "ashwagandha" in query.lower() else "unknown"
            mapping = terminology_engine.analyze_term(mock_term, detected_lang)
            jurisdiction = self._detect_jurisdiction(query)
            modules_to_use = self._plan_modules(classification.intent)
            await asyncio.sleep(0.5)

            # 4. Searching knowledge
            yield _format_sse("status", "Searching knowledge...")
            retrieved_evidence = []
            if "RAG Engine" in modules_to_use:
                retrieved_evidence = self._mock_rag_search(query)
            await asyncio.sleep(0.5)

            # 5. Reviewing evidence
            yield _format_sse("status", "Reviewing evidence...")
            evidence_eval, safe_docs = safety_orchestrator.prepare_evidence(query, retrieved_evidence)
            await asyncio.sleep(0.5)

            # 6. Generating response
            yield _format_sse("status", "Generating response...")
            generated_answer = f"Based on the analysis from {', '.join(modules_to_use)}, the findings are... [Source: Guidelines 2024]"
            validation = safety_orchestrator.post_generation_check(generated_answer, evidence_eval, retrieved_evidence)
            
            final_answer = validation.revised_response or generated_answer
            if not validation.is_valid:
                final_answer = f"Response Rejected: {validation.rejection_reason}"

            # 7. Stream token-by-token
            yield _format_sse("status", "Streaming response...")
            # Simulate token streaming
            words = final_answer.split(" ")
            for word in words:
                yield _format_sse("token", word + " ")
                await asyncio.sleep(0.05) # simulate generation delay
                
            # 8. Completion Status
            # We can optionally send the final full state
            yield _format_sse("metadata", {
                "confidence": validation.confidence_label,
                "limitations": evidence_eval.identified_gaps,
                "sources": [e.get("source") for e in retrieved_evidence if e.get("source")]
            })
            yield _format_sse("done", "[DONE]")

        except asyncio.CancelledError:
            # Client disconnected
            logger.info("Client disconnected during stream. Stopping generation.")
            raise
        except Exception as e:
            logger.error(f"Error during stream: {e}", exc_info=True)
            yield _format_sse("error", "An unexpected error occurred during processing.")
            yield _format_sse("done", "[DONE]")

ai_orchestrator = AIOrchestrator()
