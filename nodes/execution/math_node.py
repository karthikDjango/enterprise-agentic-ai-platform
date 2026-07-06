from state import GraphState
from services.math_service import solve_math


def math_node(state: GraphState) -> GraphState:
    print("✅ Math Node")

    question = state.get("question", "")

    return {
        **state,
        "response": solve_math(question),
    }