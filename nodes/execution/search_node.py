from state import GraphState

from services.search_service import search
from services.prompt_service import get_search_prompt
from services.llm_service import ask_gemini_prompt


def search_node(state: GraphState) -> GraphState:
    print("✅ Search Node")

    question = state.get("question", "")

    search_result = search(question)

    if not search_result["success"]:
        state["response"] = (
            "Unable to retrieve search results."
        )
        return state

    prompt = f"""
{get_search_prompt()}

User Question:
{question}

Search Results:
{search_result["results"]}
"""

    response = ask_gemini_prompt(prompt)

    state["response"] = response
    state["tool_used"] = search_result["provider"]

    return state