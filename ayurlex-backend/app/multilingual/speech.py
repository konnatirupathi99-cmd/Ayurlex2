from typing import Optional
from app.multilingual.models import SpeechPipelineRequest, SpeechPipelineResponse, TextPipelineRequest, VoiceState
from app.multilingual.pipeline import text_pipeline

class MultilingualSpeechPipeline:
    
    def process_voice_input(self, request: SpeechPipelineRequest) -> SpeechPipelineResponse:
        warnings = []
        
        # 1. Speech-to-Text (Modular so providers can be swapped)
        transcription, transcription_confidence = self._stt(request.audio_data)
        
        if transcription_confidence < 0.7:
            warnings.append("Some words could not be reliably transcribed. Please review the text.")
            
        # 2. Hand off to Multilingual Text Pipeline
        text_request = TextPipelineRequest(
            user_input=transcription,
            target_language_code=request.target_language_code,
            session_id=request.session_id,
            user_id=request.user_id
        )
        
        text_response = text_pipeline.process_input(text_request)
        
        # 3. Text-to-Speech
        audio_response = self._tts(text_response.translated_response or text_response.final_response, text_response.detected_language)
        
        return SpeechPipelineResponse(
            transcription=transcription,
            detected_language=text_response.detected_language,
            text_response=text_response,
            audio_response=audio_response,
            warnings=warnings + text_response.warnings
        )
        
    def _stt(self, audio_data: bytes) -> tuple[str, float]:
        # Mock STT adapter
        return ("Simulated transcription of voice input", 0.85)
        
    def _tts(self, text: str, lang_code: str) -> bytes:
        # Mock TTS adapter
        return b"simulated_audio_bytes"

speech_pipeline = MultilingualSpeechPipeline()
