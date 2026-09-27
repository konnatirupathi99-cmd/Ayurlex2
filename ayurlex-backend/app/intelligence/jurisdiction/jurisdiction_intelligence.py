from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
import re

class SourceJurisdictionContext(BaseModel):
    country: str
    region: str
    authority: str
    law_type: str
    scope: str
    effective_date: str
    version: str
    source_url: str

class JurisdictionAnalysisOutput(BaseModel):
    requested_jurisdictions: List[str]
    cross_border_issues_detected: bool
    filtered_evidence: List[Dict[str, Any]]
    conflicts_and_limitations: List[str]
    jurisdiction_warning: str

class JurisdictionIntelligenceEngine:
    def __init__(self):
        # Extensible country and region mapping
        self.supported_jurisdictions = {
            "india": ["india", "in", "bharat"],
            "united states": ["united states", "us", "usa", "america"],
            "european union": ["european union", "eu", "europe"],
            "united kingdom": ["united kingdom", "uk", "britain"],
            "international": ["international", "wipo", "global", "un"]
        }

    def _detect_jurisdictions(self, query: str) -> List[str]:
        detected = set()
        query_lower = query.lower()
        for canonical, aliases in self.supported_jurisdictions.items():
            for alias in aliases:
                # Use word boundaries to avoid partial matches like 'in' as a preposition
                if re.search(r'\b' + re.escape(alias) + r'\b', query_lower):
                    detected.add(canonical)
        
        # Default to India if no specific jurisdiction is mentioned but Ayurvedic context implies it
        if not detected:
            detected.add("india")
            
        return list(detected)

    def _filter_evidence(self, raw_evidence: List[Dict[str, Any]], target_jurisdictions: List[str]) -> List[Dict[str, Any]]:
        filtered = []
        for ev in raw_evidence:
            doc_jurisdiction = str(ev.get("metadata", {}).get("jurisdiction", "")).lower()
            if not doc_jurisdiction:
                # Keep evidence without explicit jurisdiction (e.g. classical texts) but treat carefully later
                filtered.append(ev)
                continue
                
            # Keep if the document matches one of our target jurisdictions or is explicitly International
            is_match = False
            for target in target_jurisdictions:
                if target in doc_jurisdiction or "international" in doc_jurisdiction:
                    is_match = True
                    break
            
            if is_match:
                filtered.append(ev)
                
        return filtered

    def process_query_jurisdiction(self, query: str, raw_evidence: List[Dict[str, Any]]) -> JurisdictionAnalysisOutput:
        """
        Executes the jurisdiction filtering and conflict detection pipeline.
        """
        # 1. Detect requested jurisdiction
        detected_jurisdictions = self._detect_jurisdictions(query)
        
        # 2 & 3. Retrieve and Filter unrelated sources
        filtered_evidence = self._filter_evidence(raw_evidence, detected_jurisdictions)
        
        # 4. Identify cross-border issues
        cross_border = len(detected_jurisdictions) > 1
        
        # 5. Identify conflicts or limitations
        conflicts = []
        warning = ""
        
        if cross_border:
            conflicts.append("Multiple jurisdictions requested. Note that ABS compliance and IP protection laws differ radically between these regions.")
            warning = "CRITICAL LIMITATION: Do not assume that an Indian rule applies internationally or that an international source automatically governs India. The analysis below separates the evidence strictly by regional scope."
            
        return JurisdictionAnalysisOutput(
            requested_jurisdictions=detected_jurisdictions,
            cross_border_issues_detected=cross_border,
            filtered_evidence=filtered_evidence,
            conflicts_and_limitations=conflicts,
            jurisdiction_warning=warning
        )

jurisdiction_engine = JurisdictionIntelligenceEngine()
