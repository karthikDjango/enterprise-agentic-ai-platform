from langchain_core.messages import SystemMessage

from services.llm_service import ask_gemini
from services.prompt_service import (
    get_system_prompt,
    get_conversation_prompt,
)


def chat(messages):
    """
    Generate an AI response using conversation history.
    """

    final_messages = [
        SystemMessage(content=get_system_prompt()),
        SystemMessage(content=get_conversation_prompt()),
    ]

    final_messages.extend(messages)

    response = ask_gemini(final_messages)

    return response