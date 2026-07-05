"""
Centralized Prompt Service

This service stores all prompt templates used across the platform.
No prompts should be hardcoded in nodes or other services.
"""


def get_system_prompt():
    """Base system prompt for the AI assistant."""
    return (
        "You are an Enterprise AI Assistant. "
        "Provide accurate, concise, and professional responses."
    )


def get_conversation_prompt():
    """Conversation assistant prompt."""
    return (
        "Answer the user's question naturally using the conversation history."
    )


def get_search_prompt():
    """Prompt used after retrieving search results."""
    return (
        "Use the search results to answer the user's question accurately. "
        "If the answer is not available, say you don't know."
    )


def get_intent_prompt(user_query: str):
    """Fallback prompt for intent classification."""
    return f"""
You are an Enterprise AI Router.

Return exactly one of these intents:

conversation
search
rag

Intent definitions:

conversation
- coding help
- writing assistance
- brainstorming
- opinions
- casual conversation
- questions that do not require external knowledge

search
- latest news
- current events
- recent information
- internet lookup
- information not expected to exist in company documents

rag
- questions about internal documents
- questions that should be answered using the indexed knowledge base
- company documentation
- uploaded PDFs
- uploaded text documents

Return ONLY one word.

User:
{user_query}
"""