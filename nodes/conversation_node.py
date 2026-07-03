from langchain_core.messages import HumanMessage

from state import GraphState


def conversation_node(state: GraphState) -> GraphState:
    print("✅ Conversation Node")

    question = state.get("question", "")

    messages = list(state.get("messages", []))

    messages.append(HumanMessage(content=question))

    return {
        **state,
        "messages": messages,
    }