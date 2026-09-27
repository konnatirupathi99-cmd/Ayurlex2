from typing import Dict, List, Type
from app.ai.tools.base import BaseTool

class ToolRegistry:
    """
    Registry for AYURLEX AI tools.
    Builds the system so additional tools can be added without changing the core orchestrator.
    """
    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}
        
    def register(self, tool_class: Type[BaseTool]):
        tool_instance = tool_class()
        self._tools[tool_instance.name] = tool_instance
        
    def get_tool(self, name: str) -> BaseTool:
        if name not in self._tools:
            raise ValueError(f"Tool {name} not found in registry.")
        return self._tools[name]
        
    def list_tools(self) -> List[Dict[str, str]]:
        return [{"name": t.name, "description": t.description} for t in self._tools.values()]
        
    def execute_tool(self, name: str, user_permissions: List[str], **kwargs):
        tool = self.get_tool(name)
        return tool.run(user_permissions, **kwargs)

tool_registry = ToolRegistry()
