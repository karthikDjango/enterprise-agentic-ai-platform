from services.llm_service import ask_gemini
from state import GraphState
from tools.calculator import calculate
import re
from langchain_core.messages import HumanMessage, AIMessage
from services.conversation_service import get_messages
from services.weather_service import get_weather




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
        "response": response
    }
def greeting_node(state: GraphState) -> GraphState:
    print("✅ Greeting Node")

    response = "Hello! How can I help you today?"

    # Get existing conversation history
    messages = get_messages(state)

    # Add assistant response
    messages.append(AIMessage(content=response))

    
    return {
        **state,
        "response": response,
        "messages": messages,
    }
def search_node(state: GraphState) -> GraphState:
    print("✅ Search Node")

    question = state.get("question")

    # Get existing conversation history
    messages = list(state.get("messages", []))

    print("\n===== BEFORE GEMINI =====")
    for msg in messages:
        print(f"{msg.__class__.__name__}: {msg.content}")
    print("=========================\n")

    # Add current user message to conversation history
    messages.append(HumanMessage(content=question))

    response = ask_gemini(messages)

    # Add AI response to conversation history
    messages.append(AIMessage(content=response))

    print("\n===== AFTER GEMINI =====")
    for msg in messages:
        print(f"{msg.__class__.__name__}: {msg.content}")
    print("========================\n")

    return {
        **state,
        "response": response,
        "messages": messages,
    }
def math_node(state: GraphState) -> GraphState:
    print("✅ Math Node")

    question = state.get("question")

    result = calculate(question)

    return {
        **state,
        "tool_used": "calculator",
        "response": result,
    }
def conversation_node(state: GraphState) -> GraphState:
    print("✅ Conversation Node")

    question = state.get("question", "")

    # Get existing conversation (if any)
    messages = list(state.get("messages", []))
   

    # Add current user message
    messages.append(HumanMessage(content=question))

    

    return {
        **state,
        "messages": messages
    }
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