import os
from typing import Dict, Any, List
from app.rag.models import RAGQueryRequest, RAGSystemOutput, DocumentMetadata
from app.rag.ingestion.document_loader import DocumentLoader
from app.rag.ingestion.parser import DocumentParser
from app.rag.ingestion.metadata_extractor import MetadataExtractor
from app.rag.ingestion.chunker import SemanticChunker
from app.rag.vector_store.vector_database import vector_db
from app.rag.vector_store.index_manager import keyword_index
from app.rag.vector_store.collections import CollectionManager
from app.rag.retrieval.query_analyzer import query_analyzer
from app.rag.retrieval.query_expander import query_expander
from app.rag.retrieval.metadata_filter import metadata_filter
from app.rag.retrieval.hybrid_search import hybrid_search
from app.rag.retrieval.reranker import reranker
from app.rag.evidence.evidence_validator import evidence_validator
from app.rag.evidence.evidence_ranker import evidence_ranker
from app.rag.evidence.context_builder import context_builder

class RAGService:
    def __init__(self):
        self.parser = DocumentParser()
        self.metadata_extractor = MetadataExtractor()
        self.chunker = SemanticChunker()

    def ingest_document(self, file_path: str, raw_metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full ingestion pipeline: Load -> Parse -> Metadata -> Chunk -> Embed -> Store
        """
        # Load
        loader = DocumentLoader(file_path)
        loaded_data = loader.load()
        raw_content = loaded_data["content"]
        
        # Parse & Clean
        clean_content = self.parser.parse_and_clean(raw_content)
        
        # Metadata
        merged_meta = {**loaded_data["metadata"], **raw_metadata}
        metadata = self.metadata_extractor.extract(merged_meta)
        
        # Chunk
        chunks = self.chunker.chunk_document(clean_content, metadata)
        
        # Store in Vector DB & Keyword Index
        collection_name = CollectionManager.get_collection_for_category(metadata.category)
        vector_db.add_chunks(collection_name, chunks)
        keyword_index.add_chunks(collection_name, chunks)
        
        return {
            "status": "success",
            "document_id": metadata.document_id,
            "chunks_processed": len(chunks),
            "collection": collection_name
        }

    def query(self, request: RAGQueryRequest) -> RAGSystemOutput:
        """
        Full retrieval pipeline: Analyze -> Expand -> Search -> Rerank -> Validate -> Build Context
        """
        # Analyze and expand
        analysis = query_analyzer.analyze(request)
        expanded_terms = query_expander.expand(request)
        search_query = " ".join(expanded_terms)
        
        # Build filters and determine collections
        filters = metadata_filter.build_filters(request)
        collections = CollectionManager.get_collections_for_module(request.module)
        
        # Hybrid Search
        raw_results = hybrid_search.search(collections, search_query, filters=filters, top_k=10)
        
        # Rerank
        reranked_results = reranker.rerank(raw_results, analysis)
        
        # Validate and build evidence objects
        valid_evidence, limitations = evidence_validator.validate_and_convert(reranked_results, target_jurisdiction=analysis.get("jurisdiction", "International"))
        
        # Rank final evidence
        final_evidence = evidence_ranker.rank(valid_evidence)
        
        # Assemble context output
        output = context_builder.build(
            analysis_id=request.analysis_id,
            query_analysis=analysis,
            expanded_terms=expanded_terms,
            evidence=final_evidence,
            limitations=limitations
        )
        
        return output

rag_service = RAGService()
