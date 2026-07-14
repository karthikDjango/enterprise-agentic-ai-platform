from typing import Optional
from typing_extensions import TypedDict, Annotated

from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

from models.enterprise_request import EnterpriseRequest
from models.governance_decision import GovernanceDecision
from models.security_decision import SecurityDecision


class GraphState(TypedDict):
    question: Optional[str]
    response: Optional[str]
    tool_used: Optional[str]
    intent: Optional[str]
    session_id: Optional[str]

    # AI Security decision
    security_decision: Optional[SecurityDecision]

    # Enterprise request produced by the AI
    enterprise_request: Optional[EnterpriseRequest]

    # Governance decision produced before execution
    governance_decision: Optional[GovernanceDecision]

    messages: Annotated[list[BaseMessage], add_messages]