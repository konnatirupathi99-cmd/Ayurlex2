from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

class CitationKind(str, Enum):
    CLASSICAL = "classical"
    JOURNAL = "journal"

class Citation(BaseModel):
    id: str
    title: str
    authors: str
    year: int
    source: str
    kind: CitationKind
    url: str
    doi: Optional[str] = None
    excerpt: str
    verified: bool

class SearchQuery(BaseModel):
    query: str
    limit: int = 10
