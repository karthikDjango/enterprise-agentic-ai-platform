"""
Jira Node

Responsibility:
- Receive a validated EnterpriseRequest from GraphState.
- Call the Jira Service.
- Store the response in GraphState.
"""

from state import GraphState
from services.jira_service import handle_jira_request


def jira_node(state: GraphState) -> GraphState:
    print("✅ Jira Node")

    request = state.get("enterprise_request")

    response = handle_jira_request(request)

    state["response"] = response
    state["tool_used"] = "Jira"

    return state