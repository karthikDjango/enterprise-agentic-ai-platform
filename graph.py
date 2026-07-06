from langgraph.graph import StateGraph

from state import GraphState
from nodes.router.router_node import router_node

from nodes.execution.conversation_node import conversation_node
from nodes.execution.greeting_node import greeting_node
from nodes.execution.math_node import math_node
from nodes.execution.weather_node import weather_node
from nodes.execution.search_node import search_node
from nodes.execution.rag_node import rag_node

from nodes.post_processing.conversation_history_node import (
    conversation_history_node,
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
builder.add_node(
    "conversation_history",
    conversation_history_node,
)


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