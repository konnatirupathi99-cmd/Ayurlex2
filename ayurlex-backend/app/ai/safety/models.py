from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class ConfidenceLabel(str, Enum):
    SUPPORTED = "Supported by evidence"
    PARTIALLY_SUPPORTED = "Partially supported"
    INSUFFICIENT = "Insufficient evidence"
    FURTHER_VERIFICATION = "Further verification recommended"

class EvidenceEvaluation(BaseModel):
    is_relevant: bool
    confidence_label: ConfidenceLabel
    identified_gaps: List[str] = Field(default_factory=list)
    contradictions_detected: List[str] = Field(default_factory=list)
    citation_availability: bool = False

class SafetyCheckResult(BaseModel):
    is_safe: bool
    rejection_reason: Optional[str] = None
    flags: List[str] = Field(default_factory=list)
    sanitized_content: Optional[str] = None
    needs_revision: bool = False

class ResponseValidationResult(BaseModel):
    is_valid: bool
    rejection_reason: Optional[str] = None
    confidence_label: ConfidenceLabel
    warnings: List[str] = Field(default_factory=list)
    revised_response: Optional[str] = None
