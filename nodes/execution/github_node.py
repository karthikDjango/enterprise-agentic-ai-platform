from state import GraphState
from services.github_service import GitHubService

github_service = GitHubService()


def github_node(state: GraphState) -> GraphState:
    """
    GitHub Node

    Responsibility:
    - Receive EnterpriseRequest
    - Execute GitHub Service
    - Store response in GraphState
    """

    print("✅ GitHub Node")

    request = state.get("enterprise_request")

    response = github_service.execute(request)

    state["response"] = response
    state["tool_used"] = "GitHub"

    return state