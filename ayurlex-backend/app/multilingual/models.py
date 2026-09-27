from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from enum import Enum

class LanguageDirection(str, Enum):
    LTR = "ltr"
    RTL = "rtl"

class VoiceState(str, Enum):
    IDLE = "Idle"
    LISTENING = "Listening"
    TRANSCRIBING = "Transcribing"
    UNDERSTANDING = "Understanding"
    SEARCHING = "Searching"
    GENERATING = "Generating"
    SPEAKING = "Speaking"
    COMPLETED = "Completed"
    ERROR = "Error"

class LanguageProfile(BaseModel):
    language_code: str
    language_name: str
    native_name: str
    script: str
    direction: LanguageDirection = LanguageDirection.LTR
    stt_supported: bool = True
    tts_supported: bool = True
    translation_supported: bool = True
    terminology_supported: bool = True
    enabled: bool = True

class TerminologyMapping(BaseModel):
    original_term: str
    regional_variant: Optional[str] = None
    transliteration: Optional[str] = None
    sanskrit_form: Optional[str] = None
    english_equivalent: Optional[str] = None
    scientific_name: Optional[str] = None
    synonyms: List[str] = Field(default_factory=list)
    canonical_term: str
    is_ambiguous: bool = False
    possible_matches: List[str] = Field(default_factory=list)

class TextPipelineRequest(BaseModel):
    user_input: str
    target_language_code: Optional[str] = None
    session_id: str
    user_id: str

class TextPipelineResponse(BaseModel):
    detected_language: str
    normalized_text: str
    terminology_mappings: List[TerminologyMapping]
    expanded_query: List[str]
    final_response: Optional[str] = None
    translated_response: Optional[str] = None
    citations: List[Dict[str, Any]] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)

class SpeechPipelineRequest(BaseModel):
    audio_data: bytes # In a real app this might be a file upload or stream
    target_language_code: Optional[str] = None
    session_id: str
    user_id: str

class SpeechPipelineResponse(BaseModel):
    transcription: str
    detected_language: str
    text_response: TextPipelineResponse
    audio_response: Optional[bytes] = None
    warnings: List[str] = Field(default_factory=list)
