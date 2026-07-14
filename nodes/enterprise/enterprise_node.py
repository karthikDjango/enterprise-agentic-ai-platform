from state import GraphState

from nodes.execution.github_node import github_node
from nodes.execution.jira_node import jira_node

from nodes.enterprise.enterprise_dispatcher import EnterpriseDispatcher

from services.parameter_extraction_service import ParameterExtractionService
from services.governance_service import GovernanceService
from services.ai_security_service import AISecurityService


dispatcher = EnterpriseDispatcher()
parameter_extractor = ParameterExtractionService()
governance_service = GovernanceService()
security_service = AISecurityService()


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
    1. AI Security validation
    2. Receive user request
    3. Extract EnterpriseRequest using AI
    4. Evaluate Governance
    5. Store EnterpriseRequest in GraphState
    6. Ask dispatcher which tool should execute
    7. Execute the appropriate handler
    """

    print("🏢 Enterprise Node")

    question = state.get("question", "")

    try:
        # --------------------------------------------------
        # STEP 1 : AI Security
        # --------------------------------------------------
        security_decision = security_service.evaluate(question)

        state["security_decision"] = security_decision

        print(f"Security Decision: {security_decision}")

        if not security_decision.allowed:
            state["response"] = (
                "Request blocked by AI Security.\n"
                f"Risk: {security_decision.risk}\n"
                f"Reason: {security_decision.reason}"
            )
            state["tool_used"] = "AI Security"
            return state

        # --------------------------------------------------
        # STEP 2 : AI Parameter Extraction
        # --------------------------------------------------
        request = parameter_extractor.extract(question)

        state["enterprise_request"] = request

        print(f"Enterprise Request: {request}")

        # --------------------------------------------------
        # STEP 3 : AI Governance
        # --------------------------------------------------
        governance_decision = governance_service.evaluate(request)

        state["governance_decision"] = governance_decision

        print(f"Governance Decision: {governance_decision}")

        if not governance_decision.allowed:
            state["response"] = (
                "Request blocked by AI Governance.\n"
                f"Risk: {governance_decision.risk}\n"
                f"Reason: {governance_decision.reason}"
            )
            state["tool_used"] = "Governance"
            return state

        # --------------------------------------------------
        # STEP 4 : Dispatcher
        # --------------------------------------------------
        tool = dispatcher.dispatch(request)

        print(f"Enterprise Tool Selected: {tool}")

        handler = NODE_REGISTRY.get(tool, unknown_enterprise_node)

        return handler(state)

    except Exception as e:
        state["response"] = f"Enterprise request failed: {e}"
        state["tool_used"] = "Enterprise"

        return state