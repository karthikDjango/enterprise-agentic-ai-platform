from state import GraphState

from nodes.execution.github_node import github_node
from nodes.execution.jira_node import jira_node

from nodes.enterprise.enterprise_dispatcher import EnterpriseDispatcher

from services.parameter_extraction_service import ParameterExtractionService


dispatcher = EnterpriseDispatcher()
parameter_extractor = ParameterExtractionService()


def email_node(state: GraphState) -> GraphState:
    state["response"] = "Email integration is not implemented yet."
    state["tool_used"] = "Email"
    return state


def calendar_node(state: GraphState) -> GraphState:
    state["response"] = "Calendar integration is not implemented yet."
    state["tool_used"] = "Calendar"
    return state


def unknown_enterprise_node(state: GraphState) -> GraphState:
    state["response"] = "No matching enterprise tool found."
    state["tool_used"] = "Enterprise"
    return state


NODE_REGISTRY = {
    "github": github_node,
    "jira": jira_node,
    "email": email_node,
    "calendar": calendar_node,
}


def enterprise_node(state: GraphState) -> GraphState:
    """
    Enterprise Node

    Responsibilities
    ----------------
    1. Receive user request
    2. Extract EnterpriseRequest using AI
    3. Store EnterpriseRequest in GraphState
    4. Ask dispatcher which tool should execute
    5. Execute the appropriate handler
    """

    print("🏢 Enterprise Node")

    question = state.get("question", "")

    try:
        # AI understands the request
        request = parameter_extractor.extract(question)

        # Store for downstream nodes
        state["enterprise_request"] = request

        print(f"Enterprise Request: {request}")

        # Dispatcher no longer parses English
        tool = dispatcher.dispatch(request)

        print(f"Enterprise Tool Selected: {tool}")

        handler = NODE_REGISTRY.get(tool, unknown_enterprise_node)

        return handler(state)

    except Exception as e:
        state["response"] = f"Enterprise request failed: {e}"
        state["tool_used"] = "Enterprise"

        return state