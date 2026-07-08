from services.intent_service import classify_intent
from services.vector_store_service import has_relevant_documents


def router_node(state):
    """
    Enterprise Router Node

    Responsibilities
    ----------------
    1. Determine the high-level user intent.
    2. Route General requests to either RAG or Search.
    3. Pass Enterprise requests directly to the Enterprise Domain.
    """

    user_query = state["question"]

    intent = classify_intent(user_query)

    # Only General knowledge requests go through
    # the Knowledge Domain (RAG/Search).
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