import re


def classify_intent(query: str) -> str:
    query = query.lower().strip()

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
        print(">>> Intent: greeting")
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
        print(">>> Intent: weather")
        return "weather"

    # -------------------------
    # Math
    # -------------------------
    math_pattern = r"^[0-9\s\+\-\*\/\(\)\.%]+$"

    if re.match(math_pattern, query):
        print(">>> Intent: math")
        return "math"

    # -------------------------
    # Enterprise
    # -------------------------
    enterprise_keywords = [
        "github",
        "repository",
        "repo",
        "branch",
        "commit",
        "pull request",
        "pr",
        "issue",
        "issues",
        "jira",
        "story",
        "epic",
        "sprint",
        "ticket",
        "email",
        "mail",
        "calendar",
        "meeting",
        "schedule",
        "event",
    ]

    if any(keyword in query for keyword in enterprise_keywords):
        print(">>> Intent: enterprise")
        return "enterprise"

    # -------------------------
    # Default
    # -------------------------
    print(">>> Intent: general")
    return "general"