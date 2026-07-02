import os
from dotenv import load_dotenv
import google.generativeai as genai
from langgraph.graph import StateGraph
from state import GraphState
import networkx as nx
import matplotlib.pyplot as plt

# Gemini setup...
# Load environment variables
load_dotenv()

# Read API key from .env
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, something went wrong with the Gemini API."

def classify(state: GraphState) -> GraphState:
    question = state.get("question", "").lower()
    words = question.split()

    if any(greeting in words for greeting in ["hello", "hi", "hey"]):
        classification = "greeting"
    elif "good morning" in question or "good evening" in question:
        classification = "greeting"
    else:
        classification = "search"

    return {
        **state,
        "classification": classification
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
builder = StateGraph(GraphState)

builder.add_node("classify", classify)
builder.add_node("respond", respond)

builder.set_entry_point("classify")

builder.add_edge("classify", "respond")

builder.set_finish_point("respond")

app = builder.compile()

def get_response(user_question: str) -> str:
    result = app.invoke({
        "question": user_question
    })

    return result["response"]

def visualize_workflow(builder):
    G = nx.DiGraph()

    for node in builder.nodes:
        G.add_node(node)

    for edge in builder.edges:
        G.add_edge(edge[0], edge[1])

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3000,
        node_color="skyblue",
        font_size=12,
        font_weight="bold",
        arrows=True,
    )
    plt.title("LangGraph Workflow")
    plt.show()

if __name__ == "__main__":

    visualize_workflow(builder)

    user_question = input("You: ")

    response = get_response(user_question)

    print("Bot:", response)

  
    



