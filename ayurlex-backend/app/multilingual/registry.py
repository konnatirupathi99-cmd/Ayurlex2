from typing import Dict, List, Optional
from app.multilingual.models import LanguageProfile, LanguageDirection

class LanguageRegistry:
    def __init__(self):
        self._profiles: Dict[str, LanguageProfile] = {}
        self._setup_default_languages()
        
    def _setup_default_languages(self):
        # 14 Indian Languages + English + Sanskrit
        defaults = [
            ("en", "English", "English", "Latin", LanguageDirection.LTR),
            ("hi", "Hindi", "हिन्दी", "Devanagari", LanguageDirection.LTR),
            ("te", "Telugu", "తెలుగు", "Telugu", LanguageDirection.LTR),
            ("ta", "Tamil", "தமிழ்", "Tamil", LanguageDirection.LTR),
            ("kn", "Kannada", "ಕನ್ನಡ", "Kannada", LanguageDirection.LTR),
            ("ml", "Malayalam", "മലയാളം", "Malayalam", LanguageDirection.LTR),
            ("mr", "Marathi", "मराठी", "Devanagari", LanguageDirection.LTR),
            ("bn", "Bengali", "বাংলা", "Bengali", LanguageDirection.LTR),
            ("gu", "Gujarati", "ગુજરાતી", "Gujarati", LanguageDirection.LTR),
            ("pa", "Punjabi", "ਪੰਜਾਬੀ", "Gurmukhi", LanguageDirection.LTR),
            ("or", "Odia", "ଓଡ଼ିଆ", "Odia", LanguageDirection.LTR),
            ("as", "Assamese", "অসমীয়া", "Bengali-Assamese", LanguageDirection.LTR),
            ("ur", "Urdu", "اردو", "Arabic", LanguageDirection.RTL),
            ("kok", "Konkani", "कोंकणी", "Devanagari", LanguageDirection.LTR),
            ("ks", "Kashmiri", "کٲشُر", "Arabic", LanguageDirection.RTL),
            ("sa", "Sanskrit", "संस्कृतम्", "Devanagari", LanguageDirection.LTR)
        ]
        
        for code, name, native, script, direction in defaults:
            self.register(LanguageProfile(
                language_code=code,
                language_name=name,
                native_name=native,
                script=script,
                direction=direction
            ))
            
    def register(self, profile: LanguageProfile):
        self._profiles[profile.language_code] = profile
        
    def get_profile(self, language_code: str) -> Optional[LanguageProfile]:
        return self._profiles.get(language_code.lower())
        
    def get_all_profiles(self) -> List[LanguageProfile]:
        return list(self._profiles.values())
        
    def detect_language(self, text: str) -> str:
        # Placeholder for actual language detection model (e.g., fasttext, langdetect)
        # Returns "en" as fallback if not confidently detected.
        # In a real scenario, this would analyze Unicode blocks and n-grams.
        return "en"

language_registry = LanguageRegistry()
