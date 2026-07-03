from config import model


def ask_gemini(messages):
    try:
        response = model.invoke(messages)
        return response.content

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, something went wrong with the Gemini API."
def ask_gemini_prompt(prompt: str):
    try:
        response = model.invoke(prompt)
        return response.content

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, something went wrong with the Gemini API."    
    