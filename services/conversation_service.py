from state import GraphState
from langchain_core.messages import BaseMessage

def get_messages(state: GraphState) -> list[BaseMessage]:
    return list(state.get("messages", []))