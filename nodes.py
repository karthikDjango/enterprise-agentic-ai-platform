from config import model
from state import GraphState
from tools.calculator import calculate
import re



def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, something went wrong with the Gemini API."
def classify(state: GraphState) -> GraphState:
    question = state.get("question", "").lower().strip()
    words = question.split()

    if any(greeting in words for greeting in ["hello", "hi", "hey"]):
        classification = "greeting"

    elif re.fullmatch(r"[0-9+\-*/().%\s]+", question):
        classification = "math"

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

    return {
        **state,
        "response": "Hello! How can I help you today?"
    }
def search_node(state: GraphState) -> GraphState:
    print("✅ Search Node")

    question = state.get("question")

    return {
        **state,
        "response": ask_gemini(question)
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