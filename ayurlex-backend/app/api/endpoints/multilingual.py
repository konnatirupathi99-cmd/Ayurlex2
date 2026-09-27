from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Depends
from typing import List, Dict, Any, Optional
from app.multilingual.models import (
    TextPipelineRequest, 
    TextPipelineResponse, 
    SpeechPipelineRequest, 
    SpeechPipelineResponse,
    LanguageProfile,
    TerminologyMapping
)
from app.multilingual.registry import language_registry
from app.multilingual.pipeline import text_pipeline
from app.multilingual.speech import speech_pipeline
from app.multilingual.terminology import terminology_engine

router = APIRouter(prefix="/multilingual", tags=["multilingual"])

@router.get("/languages", response_model=List[LanguageProfile])
async def get_supported_languages():
    """Retrieve all supported languages and their capabilities."""
    return language_registry.get_all_profiles()

@router.post("/text", response_model=TextPipelineResponse)
async def process_multilingual_text(request: TextPipelineRequest):
    """
    Process multilingual text: detects language, normalizes terminology, 
    expands query cross-language, and translates response.
    """
    try:
        return text_pipeline.process_input(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/speech", response_model=SpeechPipelineResponse)
async def process_multilingual_speech(
    audio: UploadFile = File(...),
    target_language_code: Optional[str] = Form(None),
    session_id: str = Form(...),
    user_id: str = Form(...)
):
    """
    ChatGPT-style voice interaction endpoint.
    Handles STT -> Text Pipeline -> TTS modularly.
    """
    try:
        audio_bytes = await audio.read()
        request = SpeechPipelineRequest(
            audio_data=audio_bytes,
            target_language_code=target_language_code,
            session_id=session_id,
            user_id=user_id
        )
        return speech_pipeline.process_voice_input(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/terminology/lookup", response_model=TerminologyMapping)
async def lookup_terminology(term: str, language_code: str = "en"):
    """
    Directly query the Ayurvedic Terminology Intelligence engine for canonical mappings.
    """
    return terminology_engine.analyze_term(term, language_code)
