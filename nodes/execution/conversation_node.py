from state import GraphState
from services.conversation_service import chat
from services.memory_service import (
    add_user_message,
    add_ai_message,
    get_messages,
)
from services.conversation_history_service import save_conversation


def conversation_node(state: GraphState) -> GraphState:
    print("✅ Conversation Node")

    question = state.get("question", "")
    session_id = state["session_id"]

    # Save user message to memory
    state = add_user_message(state, question)

    
    # Get conversation history
    messages = get_messages(state)

    # Generate AI response
    response = chat(messages)

    # Save AI response to memory
    state = add_ai_message(state, response)

    save_conversation(
    session_id=session_id,
    question=question,
    response=response,
    )
    state["response"] = response

    return state