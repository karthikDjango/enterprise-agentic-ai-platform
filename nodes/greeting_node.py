from langchain_core.messages import AIMessage

from state import GraphState
from services.conversation_service import get_messages


def greeting_node(state: GraphState) -> GraphState:
    print("✅ Greeting Node")

    response = "Hello! How can I help you today?"

    messages = get_messages(state)
    messages.append(AIMessage(content=response))

    return {
        **state,
        "response": response,
        "messages": messages,
    }