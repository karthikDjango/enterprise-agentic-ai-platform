from typing import Optional
from typing_extensions import TypedDict


class GraphState(TypedDict):
    question: Optional[str]
    classification: Optional[str]
    response: Optional[str]
    tool_used: Optional[str]