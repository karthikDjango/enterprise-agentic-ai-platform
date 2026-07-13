"""
Jira Node

Responsibility:
- Receive a validated EnterpriseRequest from GraphState.
- Call the Jira Service.
- Store the response in GraphState.
"""

from state import GraphState
from services.jira_service import JiraService

jira_service = JiraService()


def jira_node(state: GraphState) -> GraphState:
    print("✅ Jira Node")

    request = state.get("enterprise_request")

    response = jira_service.execute(request)

    state["response"] = response
    state["tool_used"] = "Jira"

    return state