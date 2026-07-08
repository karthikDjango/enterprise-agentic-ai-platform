import sqlite3

DATABASE_NAME = "chatbot.db"


def initialize_database():
    """
    Create the SQLite database and conversation_history table.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS conversation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()


def save_message(session_id: str, role: str, message: str):
    """
    Save one message.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO conversation_history
        (session_id, role, message)
        VALUES (?, ?, ?)
        """,
        (session_id, role, message),
    )

    connection.commit()
    connection.close()


def load_conversation(session_id: str):
    """
    Load conversation history.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT role, message, created_at
        FROM conversation_history
        WHERE session_id = ?
        ORDER BY id ASC
        """,
        (session_id,),
    )

    conversations = cursor.fetchall()

    connection.close()

    return conversations


def delete_conversation(session_id: str):
    """
    Delete a conversation.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM conversation_history
        WHERE session_id = ?
        """,
        (session_id,),
    )

    connection.commit()
    connection.close()