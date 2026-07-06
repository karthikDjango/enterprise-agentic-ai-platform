from services.database_service import save_message


def save_conversation(
    session_id: str,
    question: str,
    response: str,
):
    """
    Persist a complete conversation exchange.
    """

    save_message(
        session_id=session_id,
        role="user",
        message=question,
    )

    save_message(
        session_id=session_id,
        role="assistant",
        message=response,
    )