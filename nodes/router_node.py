from services.intent_service import classify_intent
from services.vector_store_service import has_relevant_documents


def router_node(state):
    """
    Enterprise Router Node

    This is the single entry point of the application.
    It determines the user's intent and stores it in the state.
    """

    user_query = state["question"]

    intent = classify_intent(user_query)

    # Decide between RAG and Search
    if intent == "general":
        if has_relevant_documents(user_query):
            intent = "rag"
        else:
            intent = "search"

    print("\n===== ROUTER =====")
    print(f"Question : {user_query}")
    print(f"Intent   : {intent}")
    print("==================\n")

    state["intent"] = intent

    return state