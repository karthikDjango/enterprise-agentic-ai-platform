from typing import Optional
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage


class GraphState(TypedDict):
    question: Optional[str]
    response: Optional[str]
    tool_used: Optional[str]
    intent: Optional[str]
    messages: Annotated[list[BaseMessage], add_messages]