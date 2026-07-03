from langchain_core.messages import HumanMessage, AIMessage

from state import GraphState
from services.llm_service import ask_gemini


def search_node(state: GraphState) -> GraphState:
    print("✅ Search Node")

    question = state.get("question")

    messages = list(state.get("messages", []))

    print("\n===== BEFORE GEMINI =====")
    for msg in messages:
        print(f"{msg.__class__.__name__}: {msg.content}")
    print("=========================\n")

    messages.append(HumanMessage(content=question))

    response = ask_gemini(messages)

    messages.append(AIMessage(content=response))

    print("\n===== AFTER GEMINI =====")
    for msg in messages:
        print(f"{msg.__class__.__name__}: {msg.content}")
    print("========================\n")

    return {
        **state,
        "response": response,
        "messages": messages,
    }