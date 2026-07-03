from langgraph.graph import StateGraph

from state import GraphState
from nodes import (
    classify,
    greeting_node,
    search_node,
    math_node,
    weather_node,
)
from langgraph.checkpoint.memory import MemorySaver



def route(state):
    classification = state["classification"]

    if classification == "greeting":
        return "greeting"

    elif classification == "math":
        return "math"

    elif classification == "weather":
        return "weather"

    return "search"


# Build the graph
builder = StateGraph(GraphState)

# Register nodes
builder.add_node("weather", weather_node)
builder.add_node("classify", classify)
builder.add_node("greeting", greeting_node)
builder.add_node("search", search_node)
builder.add_node("math", math_node)

# Entry point
builder.set_entry_point("classify")


# Conditional routing
builder.add_conditional_edges(
    "classify",
    route,
    {
        "greeting": "greeting",
        "math": "math",
        "weather": "weather",
        "search": "search",
    },
)

# Finish points
builder.set_finish_point("greeting")
builder.set_finish_point("search")
builder.set_finish_point("math")
builder.set_finish_point("weather")


# Compile
memory = MemorySaver()

app = builder.compile(
    checkpointer=memory
)