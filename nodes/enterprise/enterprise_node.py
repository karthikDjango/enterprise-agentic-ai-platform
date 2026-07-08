from state import GraphState

from nodes.execution.github_node import github_node
from nodes.enterprise.enterprise_dispatcher import EnterpriseDispatcher
from nodes.execution.jira_node import jira_node


dispatcher = EnterpriseDispatcher()





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


# Registry of Enterprise Tool Handlers
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
    1. Receive GraphState
    2. Ask the dispatcher which enterprise tool is needed
    3. Execute the correct handler from the registry
    """

    print("🏢 Enterprise Node")

    question = state.get("question", "")

    tool = dispatcher.dispatch(question)

    print(f"Enterprise Tool Selected: {tool}")

    handler = NODE_REGISTRY.get(tool, unknown_enterprise_node)

    return handler(state)