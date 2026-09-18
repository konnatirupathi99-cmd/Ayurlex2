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
        # Placeholder for pdfplumber extraction
        # e.g., with pdfplumber.open(self.file_path) as pdf: return "".join(page.extract_text() for page in pdf.pages)
        return "PDF content extracted (stub)"
        
    def _load_docx(self) -> str:
        # Placeholder for python-docx extraction
        # e.g., doc = docx.Document(self.file_path); return "\n".join([p.text for p in doc.paragraphs])
        return "DOCX content extracted (stub)"
        
    def _load_html(self) -> str:
        # Placeholder for BeautifulSoup extraction
        # e.g., soup = BeautifulSoup(html_content, 'html.parser'); return soup.get_text()
        return "HTML content extracted (stub)"
