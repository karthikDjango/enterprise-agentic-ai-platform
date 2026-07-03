from state import GraphState
from services.llm_service import ask_gemini


def respond(state: GraphState) -> GraphState:
    classification = state.get("classification")
    question = state.get("question")

    if classification == "greeting":
        response = "Hello! How can I help you today?"
    elif classification == "search":
        response = ask_gemini(question)
    else:
        response = "I'm not sure how to respond to that."

    return {
        **state,
        "response": response,
    }