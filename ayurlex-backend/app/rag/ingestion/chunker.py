import uuid
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.models import DocumentMetadata, ChunkMetadata

class SemanticChunker:
    """
    Intelligent chunking system that preserves meaning and paragraph relationships.
    """
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )

    def chunk_document(self, text: str, metadata: DocumentMetadata) -> List[ChunkMetadata]:
        if not text:
            return []
            
        chunks = self.splitter.split_text(text)
        chunk_metadata_list = []
        
        for i, chunk_text in enumerate(chunks):
            # In a more advanced implementation, section_title and page_number would be parsed
            chunk_meta = ChunkMetadata(
                chunk_id=str(uuid.uuid4()),
                document_id=metadata.document_id,
                content=chunk_text,
                chunk_index=i,
                section_title=None, 
                page_number=None,
                language=metadata.language,
                category=metadata.category,
                jurisdiction=metadata.jurisdiction
            )
            chunk_metadata_list.append(chunk_meta)
            
        return chunk_metadata_list
