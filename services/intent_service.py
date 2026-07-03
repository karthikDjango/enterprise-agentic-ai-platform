from services.llm_service import ask_gemini_prompt


def classify_intent(user_query: str) -> str:
    prompt = f"""
You are an intent classifier.

Classify the user's request into ONE category.

Categories:
- SEARCH
- CHAT

Rules:
- SEARCH: User is asking for facts, latest news, weather, sports, information, internet lookup, current events.
- CHAT: Greetings, conversation, explanations, coding help, brainstorming, writing.

Return ONLY one word.

User:
{user_query}
"""

    response = ask_gemini_prompt(prompt)

    return response.strip().upper()