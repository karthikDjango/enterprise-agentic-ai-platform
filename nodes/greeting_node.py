from state import GraphState
from services.greeting_service import get_greeting


def greeting_node(state: GraphState) -> GraphState:
    print("✅ Greeting Node")

    return {
        **state,
        "response": get_greeting(),
    }