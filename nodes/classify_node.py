import re

from state import GraphState


def classify(state: GraphState) -> GraphState:
    question = state.get("question", "").lower().strip()
    words = question.split()

    if any(greeting in words for greeting in ["hello", "hi", "hey"]):
        classification = "greeting"

    elif re.fullmatch(r"[0-9+\-*/().%\s]+", question):
        classification = "math"

    elif "weather" in question:
        classification = "weather"

    else:
        classification = "search"

    return {
        **state,
        "classification": classification,
    }