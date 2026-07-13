from config import model


def ask_gemini(messages):
    """
    Chat with Gemini using LangChain messages.
    """

    try:
        response = model.invoke(messages)
        return response.content

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, something went wrong with the Gemini API."


def ask_gemini_prompt(prompt: str):
    """
    Send a raw prompt to Gemini.

    Used by:
    - Intent classification
    - Parameter extraction
    - Any prompt-based services
    """

    try:
        # Temporary debugging
        print("\n========== GEMINI PROMPT ==========")
        print(prompt)

        response = model.invoke(prompt)

        print("\n========== GEMINI RAW RESPONSE ==========")
        print(repr(response.content))

        return response.content

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, something went wrong with the Gemini API."