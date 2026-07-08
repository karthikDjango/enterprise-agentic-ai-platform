from state import GraphState
from services.github_service import GitHubService


github_service = GitHubService()


def github_node(state: GraphState) -> GraphState:
    """
    GitHub Node

    Responsibility:
    - Receive GraphState
    - Call GitHub Service
    - Store response in GraphState
    """

    print("✅ GitHub Node")

    repository = github_service.get_repository_details()

    response = (
        f"Repository: {repository['full_name']}\n"
        f"Description: {repository['description']}\n"
        f"Language: {repository['language']}\n"
        f"Stars: {repository['stars']}\n"
        f"Open Issues: {repository['open_issues']}\n"
        f"Default Branch: {repository['default_branch']}\n"
        f"URL: {repository['url']}"
    )

    state["response"] = response
    state["tool_used"] = "GitHub"

    return state