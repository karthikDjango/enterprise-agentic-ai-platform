from state import GraphState
from tools.calculator import calculate


def math_node(state: GraphState) -> GraphState:
    print("✅ Math Node")

    question = state.get("question")

    result = calculate(question)

    return {
        **state,
        "tool_used": "calculator",
        "response": result,
    }