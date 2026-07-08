from state import GraphState


def tool_dispatcher_node(state: GraphState) -> str:
    """
    Enterprise Tool Dispatcher

    Responsibility:
    Decide which execution node should
    handle the requested tool.
    """

    tool = state.get("tool_used", "").lower()

    tool_routes = {
        "github": "github",
        "weather": "weather",
        "math": "math",
        "search": "search",
        "rag": "rag",
    }

    return tool_routes.get(tool, "conversation")