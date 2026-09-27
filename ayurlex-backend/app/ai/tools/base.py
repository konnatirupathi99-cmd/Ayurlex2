from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class ToolResult(BaseModel):
    tool_name: str
    status: str # e.g. "success", "error", "no_result"
    source: str
    data: Any
    limitations: List[str] = Field(default_factory=list)
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

class BaseTool(ABC):
    """
    Abstract base class for all AYURLEX AI tools.
    """
    name: str = "base_tool"
    description: str = "Base tool description"
    required_permissions: List[str] = []
    
    def __init__(self):
        pass

    def check_permissions(self, user_permissions: List[str]) -> bool:
        """
        Tool permissions should be controlled by the backend.
        """
        for req_perm in self.required_permissions:
            if req_perm not in user_permissions:
                return False
        return True

    def run(self, user_permissions: List[str], **kwargs) -> ToolResult:
        """
        Executes the tool with permissions check, logging, and error handling.
        """
        # 1. Permission check
        if not self.check_permissions(user_permissions):
            logger.warning(f"Permission denied for tool {self.name}")
            return ToolResult(
                tool_name=self.name,
                status="error_permission_denied",
                source="system",
                data=None,
                limitations=["User does not have permission to execute this tool."]
            )
            
        # 2. Execution & Logging
        logger.info(f"Executing tool {self.name} with args: {kwargs}")
        try:
            result = self.execute(**kwargs)
            logger.info(f"Tool {self.name} executed successfully. Status: {result.status}")
            return result
        except Exception as e:
            logger.error(f"Error executing tool {self.name}: {str(e)}", exc_info=True)
            return ToolResult(
                tool_name=self.name,
                status="error",
                source="system",
                data=None,
                limitations=[f"Execution failed: {str(e)}"]
            )
            
    @abstractmethod
    def execute(self, **kwargs) -> ToolResult:
        """
        The actual tool logic to be implemented by subclasses.
        Must return a ToolResult.
        """
        pass
