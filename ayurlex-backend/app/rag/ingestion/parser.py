import re

class DocumentParser:
    """
    Cleans raw text and normalizes whitespace and encoding.
    """
    def parse_and_clean(self, raw_content: str) -> str:
        if not raw_content:
            return ""
            
        # Remove null bytes
        content = raw_content.replace('\x00', '')
        
        # Normalize whitespace (multiple spaces to single space)
        content = re.sub(r'[ \t]+', ' ', content)
        
        # Normalize newlines (multiple newlines to double newline)
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        # Strip leading/trailing whitespace
        content = content.strip()
        
        return content
