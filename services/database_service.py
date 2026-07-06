import sqlite3

DATABASE_NAME = "chatbot.db"


def initialize_database():
    """
    Creates the SQLite database and conversation_history table
    if they do not already exist.
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
def save_message(session_id: str, role: str, message: str):
    """
    Saves a single message to the conversation_history table.
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

def load_conversation(session_id: str):
    """
    Loads all messages for a given session.
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

def delete_conversation(session_id: str):
    """
    Deletes all messages for a given session.
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



    return conversations   
    connection.commit()
    connection.close()