from graph import app


def get_response(user_question: str) -> str:
    result = app.invoke(
        {
            "question": user_question
        }
    )

    return result["response"]


if __name__ == "__main__":

    print("🤖 LangGraph Agent")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        response = get_response(question)

        print(f"Bot: {response}\n")