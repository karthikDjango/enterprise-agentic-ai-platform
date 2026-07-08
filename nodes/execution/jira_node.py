"""
Jira Node

Responsibility:
- Receive requests from the Enterprise Node.
- Call the Jira Service.
- Store the response in the graph state.
"""

from state import GraphState
from services.jira_service import handle_jira_request


def jira_node(state: GraphState) -> GraphState:
    print("✅ Jira Node")

    question = state.get("question", "")

    response = handle_jira_request(question)

    state["response"] = response
    state["tool_used"] = "Jira"

    return state