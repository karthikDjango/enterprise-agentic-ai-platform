from state import GraphState
from services.conversation_service import chat
from services.memory_service import (
    add_user_message,
    add_ai_message,
    get_messages,
)


def conversation_node(state: GraphState) -> GraphState:
    print("✅ Conversation Node")

    question = state.get("question", "")

    # Save user message
    state = add_user_message(state, question)

    # Get conversation history
    messages = get_messages(state)

    # Generate AI response
    response = chat(messages)

    # Save AI response
    state = add_ai_message(state, response)

    state["response"] = response

    return state