from state import GraphState
from services.weather_service import get_weather


def weather_node(state: GraphState) -> GraphState:
    print("✅ Weather Node")

    question = state.get("question", "").lower()

    # Simple city extraction (we'll improve this later)
    city = (
        question.replace("what is the weather in", "")
        .replace("what's the weather in", "")
        .replace("weather in", "")
        .strip()
        .title()
    )

    if not city:
        response = "Please specify a city."
    else:
        response = get_weather(city)

    return {
        **state,
        "response": response,
    }