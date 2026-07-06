from state import GraphState
from services.conversation_history_service import save_conversation


def conversation_history_node(state: GraphState) -> GraphState:
    """
    Persist the completed conversation.
    """

    session_id = state["session_id"]
    question = state["question"]
    response = state["response"]

    save_conversation(
        session_id=session_id,
        question=question,
        response=response,
    )

    return state