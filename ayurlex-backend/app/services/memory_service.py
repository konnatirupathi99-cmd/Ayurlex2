import json
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.models.memory import ShortTermMemory, LongTermMemory, Message, MemoryRetrievalRequest
# In a real app, you'd use a real LLM utility, we mock the summarizer here
# from app.rag.embeddings.embedding_service import embedding_service if needed for vector search of memory

class MemoryService:
    def __init__(self):
        # In-memory storage for demonstration.
        # Structure: user_id -> session_id -> ShortTermMemory
        self.stm_store: Dict[str, Dict[str, ShortTermMemory]] = {}
        # Structure: user_id -> LongTermMemory
        self.ltm_store: Dict[str, LongTermMemory] = {}
        
        self.MAX_CONTEXT_MESSAGES = 10  # Context window management limit
        
    def _get_or_create_stm(self, user_id: str, session_id: str) -> ShortTermMemory:
        if user_id not in self.stm_store:
            self.stm_store[user_id] = {}
        if session_id not in self.stm_store[user_id]:
            self.stm_store[user_id][session_id] = ShortTermMemory(
                session_id=session_id, 
                user_id=user_id
            )
        return self.stm_store[user_id][session_id]
        
    def _get_or_create_ltm(self, user_id: str) -> LongTermMemory:
        if user_id not in self.ltm_store:
            self.ltm_store[user_id] = LongTermMemory(user_id=user_id)
        return self.ltm_store[user_id]

    def add_message(self, user_id: str, session_id: str, role: str, content: str) -> ShortTermMemory:
        stm = self._get_or_create_stm(user_id, session_id)
        
        message = Message(role=role, content=content)
        stm.messages.append(message)
        stm.last_updated = datetime.utcnow().isoformat()
        
        self._manage_context_window(stm)
        return stm
        
    def _manage_context_window(self, stm: ShortTermMemory):
        """
        Context-window management: if conversation is too long, 
        summarize older messages and keep only recent ones.
        """
        if len(stm.messages) > self.MAX_CONTEXT_MESSAGES:
            # We would call an LLM here to summarize:
            # summary = llm.summarize(stm.summary, stm.messages[:-5])
            
            # Mocking summarization:
            older_messages = stm.messages[:-5]
            recent_messages = stm.messages[-5:]
            
            extracted_info = " ".join([m.content[:50] for m in older_messages])
            
            if stm.summary:
                stm.summary += f" | {extracted_info}..."
            else:
                stm.summary = f"Summary of earlier conversation: {extracted_info}..."
                
            # Keep only the last 5 messages
            stm.messages = recent_messages
            
    def update_context(self, user_id: str, session_id: str, 
                       task: Optional[str] = None, 
                       language: Optional[str] = None,
                       jurisdiction: Optional[str] = None,
                       analysis_context: Optional[Dict[str, Any]] = None) -> ShortTermMemory:
        stm = self._get_or_create_stm(user_id, session_id)
        if task: stm.current_task = task
        if language: stm.current_language = language
        if jurisdiction: stm.current_jurisdiction = jurisdiction
        if analysis_context: 
            stm.current_analysis_context.update(analysis_context)
        stm.last_updated = datetime.utcnow().isoformat()
        return stm

    def update_ltm(self, user_id: str, preferences: Dict[str, Any]) -> LongTermMemory:
        """
        Update long-term user preferences safely.
        """
        ltm = self._get_or_create_ltm(user_id)
        
        if "preferred_language" in preferences:
            ltm.preferred_language = preferences["preferred_language"]
        if "frequently_used_jurisdiction" in preferences:
            ltm.frequently_used_jurisdiction = preferences["frequently_used_jurisdiction"]
        if "interface_preferences" in preferences:
            ltm.interface_preferences.update(preferences["interface_preferences"])
        if "saved_analysis_preferences" in preferences:
            ltm.saved_analysis_preferences.update(preferences["saved_analysis_preferences"])
            
        ltm.last_updated = datetime.utcnow().isoformat()
        return ltm

    def retrieve_relevant_memory(self, request: MemoryRetrievalRequest) -> Dict[str, Any]:
        """
        Allow the AI orchestrator to request only the memory relevant to the current query.
        """
        result = {}
        
        if request.include_long_term:
            ltm = self.ltm_store.get(request.user_id)
            if ltm:
                result["long_term_preferences"] = ltm.model_dump(exclude={"user_id"})
                
        if request.include_short_term and request.session_id:
            stm = self.stm_store.get(request.user_id, {}).get(request.session_id)
            if stm:
                # If a query is provided, we could theoretically do semantic search 
                # over the messages. For now, we return the managed context window.
                # The _manage_context_window ensures it's not excessively long.
                result["short_term_context"] = {
                    "summary": stm.summary,
                    "recent_messages": [m.model_dump() for m in stm.messages],
                    "current_task": stm.current_task,
                    "current_language": stm.current_language,
                    "current_jurisdiction": stm.current_jurisdiction,
                    "current_analysis_context": stm.current_analysis_context
                }
                
        return result

    def delete_session_memory(self, user_id: str, session_id: str) -> bool:
        if user_id in self.stm_store and session_id in self.stm_store[user_id]:
            del self.stm_store[user_id][session_id]
            return True
        return False

    def clear_long_term_memory(self, user_id: str) -> bool:
        if user_id in self.ltm_store:
            del self.ltm_store[user_id]
            return True
        return False

memory_service = MemoryService()
