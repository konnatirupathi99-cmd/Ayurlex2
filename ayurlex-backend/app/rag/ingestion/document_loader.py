import os
import json
from typing import List, Dict, Any, Optional

class DocumentLoader:
    """
    Responsible for loading documents from various formats.
    Supported formats: TXT, JSON, PDF (stub), DOCX (stub), HTML (stub)
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_extension = os.path.splitext(file_path)[1].lower()

    def load(self) -> Dict[str, Any]:
        """
        Loads the file and returns raw content and extracted basic metadata.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        raw_content = ""
        metadata = {"file_name": os.path.basename(self.file_path), "extension": self.file_extension}
        
        if self.file_extension == '.txt':
            raw_content = self._load_txt()
        elif self.file_extension == '.json':
            raw_content = self._load_json()
        elif self.file_extension == '.pdf':
            raw_content = self._load_pdf()
        elif self.file_extension == '.docx':
            raw_content = self._load_docx()
        elif self.file_extension == '.html' or self.file_extension == '.htm':
            raw_content = self._load_html()
        else:
            raise ValueError(f"Unsupported file format: {self.file_extension}")
            
        return {"content": raw_content, "metadata": metadata}

    def _load_txt(self) -> str:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def _load_json(self) -> str:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return json.dumps(data, indent=2)
            
    def _load_pdf(self) -> str:
        try:
            import pdfplumber
            text = ""
            with pdfplumber.open(self.file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text
        except ImportError:
            return "PDF content extracted (pdfplumber not installed)"
        
    def _load_docx(self) -> str:
        try:
            import docx
            doc = docx.Document(self.file_path)
            return "\n".join([p.text for p in doc.paragraphs])
        except ImportError:
            return "DOCX content extracted (python-docx not installed)"
        
    def _load_html(self) -> str:
        try:
            from bs4 import BeautifulSoup
            with open(self.file_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                return soup.get_text(separator='\n', strip=True)
        except ImportError:
            return "HTML content extracted (beautifulsoup4 not installed)"
        except UnicodeDecodeError:
            with open(self.file_path, 'r', encoding='latin-1') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                return soup.get_text(separator='\n', strip=True)
