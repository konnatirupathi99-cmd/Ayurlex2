from typing import List

def detect_language(query: str, ingredients: List[str]) -> str:
    """
    Detects language of the user input.
    For this prototype, it uses a basic mock detection.
    """
    combined_text = query + " " + " ".join(ingredients)
    
    # Basic mock rules
    if any(char >= '\u0900' and char <= '\u097F' for char in combined_text):
        return "hi" # Hindi
    if any(char >= '\u0C00' and char <= '\u0C7F' for char in combined_text):
        return "te" # Telugu
        
    return "en" # Default English
