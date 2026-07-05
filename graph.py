from langgraph.graph import StateGraph

from state import GraphState
from nodes import (
    router_node,
    conversation_node,
    greeting_node,
    math_node,
    weather_node,
    search_node,
    rag_node,
)



from langgraph.checkpoint.memory import MemorySaver



def route(state):
    return state["intent"]


# Build the graph
builder = StateGraph(GraphState)

# Register nodes
builder.add_node("weather", weather_node)
builder.add_node("conversation", conversation_node)
builder.add_node("router", router_node)
builder.add_node("greeting", greeting_node)
builder.add_node("math", math_node)
builder.add_node("search", search_node)
builder.add_node("rag", rag_node)


# Entry point
builder.set_entry_point("router")


# Conditional routing

builder.add_conditional_edges(
    "router",
    route,
    {
        "greeting": "greeting",
        "math": "math",
        "weather": "weather",
        "conversation": "conversation",
        "search": "search",
        "rag": "rag",
    },
)

# Finish points
builder.set_finish_point("greeting")
builder.set_finish_point("conversation")
builder.set_finish_point("math")
builder.set_finish_point("weather")
builder.set_finish_point("search")
builder.set_finish_point("rag")


# Compile
memory = MemorySaver()

app = builder.compile(
    checkpointer=memory
)