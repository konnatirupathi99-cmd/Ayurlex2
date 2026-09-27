from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class AyurvedicTermDefinition(BaseModel):
    canonical_term: str
    scientific_name: str
    english_name: Optional[str] = None
    hindi_name: Optional[str] = None
    telugu_name: Optional[str] = None
    sanskrit_name: Optional[str] = None
    regional_variants: List[str] = Field(default_factory=list)
    transliterations: List[str] = Field(default_factory=list)
    synonyms: List[str] = Field(default_factory=list)
    aliases: List[str] = Field(default_factory=list)
    formulation_associations: List[str] = Field(default_factory=list)
    traditional_uses: List[str] = Field(default_factory=list)
    ambiguity_status: bool = False
    evidence_source_ids: List[str] = Field(default_factory=list)

class TerminologyOutput(BaseModel):
    original_term: str
    normalized_term: str
    candidate_matches: List[AyurvedicTermDefinition]
    scientific_name: Optional[str] = None
    language: str
    confidence: str # High, Medium, Low
    ambiguity: bool
    sources: List[str]

class AyurvedicTerminologyEngine:
    def __init__(self):
        # Mock database for demonstration
        self._mock_db = {
            "guduchi": AyurvedicTermDefinition(
                canonical_term="Guduchi",
                scientific_name="Tinospora cordifolia",
                english_name="Heart-leaved moonseed",
                hindi_name="Giloy",
                sanskrit_name="Amrita",
                regional_variants=["Gulvel"],
                synonyms=["Galo"],
                ambiguity_status=False,
                evidence_source_ids=["API_VOL_1", "TKDL_TINOSPORA"]
            ),
            "brahmi": AyurvedicTermDefinition(
                canonical_term="Brahmi",
                scientific_name="Bacopa monnieri", # OR Centella asiatica (Gotu Kola) - Ambiguous!
                english_name="Water hyssop",
                hindi_name="Jalnim",
                sanskrit_name="Brahmi",
                ambiguity_status=True,
                evidence_source_ids=["API_VOL_2"]
            )
        }

    def _detect_language(self, term: str) -> str:
        # Mock detection
        if any("\u0900" <= c <= "\u097F" for c in term):
            return "hi" # Hindi Devanagari
        return "en" # Fallback

    def _normalize(self, term: str) -> str:
        return term.strip().lower()

    def _transliterate(self, term: str, lang: str) -> str:
        # In a real system, transliterate Indic text to Latin script
        return term

    def _expand_synonyms(self, term: str) -> List[str]:
        # Would query the DB for synonyms pointing to canonical terms
        if term == "giloy":
            return ["guduchi"]
        return [term]

    def process_term(self, user_term: str) -> TerminologyOutput:
        """
        Executes the terminology intelligence flow.
        """
        # 1. Language detection
        lang = self._detect_language(user_term)
        
        # 2. Normalization
        norm_term = self._normalize(user_term)
        
        # 3. Transliteration
        trans_term = self._transliterate(norm_term, lang)
        
        # 4. Synonym expansion
        expanded_terms = self._expand_synonyms(trans_term)
        
        # 5. Canonical mapping
        candidates = []
        for t in expanded_terms:
            if t in self._mock_db:
                candidates.append(self._mock_db[t])
                
        if not candidates:
            return TerminologyOutput(
                original_term=user_term,
                normalized_term=norm_term,
                candidate_matches=[],
                language=lang,
                confidence="Low",
                ambiguity=False,
                sources=[]
            )
            
        # If multiple candidates or the candidate itself is ambiguous
        is_ambiguous = len(candidates) > 1 or any(c.ambiguity_status for c in candidates)
        
        # 6. Scientific Mapping & 7. Confidence Score
        confidence = "High" if not is_ambiguous else "Low"
        scientific_name = candidates[0].scientific_name if not is_ambiguous else None
        
        # Never silently convert an ambiguous term!
        if is_ambiguous:
            scientific_name = None
            
        sources = list(set([src for c in candidates for src in c.evidence_source_ids]))

        return TerminologyOutput(
            original_term=user_term,
            normalized_term=norm_term,
            candidate_matches=candidates,
            scientific_name=scientific_name,
            language=lang,
            confidence=confidence,
            ambiguity=is_ambiguous,
            sources=sources
        )

terminology_engine = AyurvedicTerminologyEngine()
