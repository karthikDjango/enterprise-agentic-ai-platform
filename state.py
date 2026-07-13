from typing import Optional
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

from models.enterprise_request import EnterpriseRequest


class GraphState(TypedDict):
    question: Optional[str]
    response: Optional[str]
    tool_used: Optional[str]
    intent: Optional[str]
    session_id: Optional[str]

    # NEW
    enterprise_request: Optional[EnterpriseRequest]

    messages: Annotated[list[BaseMessage], add_messages]