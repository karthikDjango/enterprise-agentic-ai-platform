from state import GraphState

from nodes.execution.github_node import github_node
from nodes.execution.jira_node import jira_node

from nodes.enterprise.enterprise_dispatcher import EnterpriseDispatcher

from services.parameter_extraction_service import ParameterExtractionService
from services.governance_service import GovernanceService


dispatcher = EnterpriseDispatcher()
parameter_extractor = ParameterExtractionService()
governance_service = GovernanceService()


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
    3. Evaluate Governance
    4. Store EnterpriseRequest in GraphState
    5. Ask dispatcher which tool should execute
    6. Execute the appropriate handler
    """

    print("🏢 Enterprise Node")

    question = state.get("question", "")

    try:
        # AI understands the request
        request = parameter_extractor.extract(question)

        # Store request for downstream nodes
        state["enterprise_request"] = request

        print(f"Enterprise Request: {request}")

        # Evaluate governance policies
        governance_decision = governance_service.evaluate(request)

        # Store governance decision
        state["governance_decision"] = governance_decision

        print(f"Governance Decision: {governance_decision}")

        # Stop execution if governance blocks the request
        if not governance_decision.allowed:
            state["response"] = (
                "Request blocked by AI Governance.\n"
                f"Risk: {governance_decision.risk}\n"
                f"Reason: {governance_decision.reason}"
            )
            state["tool_used"] = "Governance"
            return state

        # Dispatcher selects the execution node
        tool = dispatcher.dispatch(request)

        print(f"Enterprise Tool Selected: {tool}")

        handler = NODE_REGISTRY.get(tool, unknown_enterprise_node)

        return handler(state)

    except Exception as e:
        state["response"] = f"Enterprise request failed: {e}"
        state["tool_used"] = "Enterprise"

        return state