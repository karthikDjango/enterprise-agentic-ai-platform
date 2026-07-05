print(">>> LOADED NEW intent_service.py")

import re


def classify_intent(user_query: str) -> str:
    """
    Enterprise Intent Router

    Rule-based routing first.
    Everything else is treated as a general knowledge request.
    The Router Node will decide whether to use RAG or Search.
    """

    query = user_query.lower().strip()
    print(">>> classify_intent() called")
    # -------------------------
    # Greeting
    # -------------------------
    greetings = {
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
    }

    if query in greetings:
        return "greeting"

    # -------------------------
    # Weather
    # -------------------------
    weather_keywords = [
        "weather",
        "temperature",
        "forecast",
        "rain",
        "climate",
    ]

    if any(word in query for word in weather_keywords):
        return "weather"

    # -------------------------
    # Math
    # -------------------------
    math_pattern = r"^[0-9\s\+\-\*\/\(\)\.%]+$"

    if re.match(math_pattern, query):
        return "math"

    # -------------------------
    # Default Routing
    # -------------------------
    return "general"