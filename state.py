from typing import Optional, Annotated
from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class GraphState(TypedDict):
    question: Optional[str]
    classification: Optional[str]
    response: Optional[str]
    tool_used: Optional[str]
    messages: Annotated[list[BaseMessage], add_messages]