from state import GraphState
from services.rag_service import rag_search


def rag_node(state: GraphState) -> GraphState:
    print("📚 RAG Node")

    question = state["question"]

    response = rag_search(question)

    state["response"] = response

    return state