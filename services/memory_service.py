from langchain_core.messages import HumanMessage, AIMessage


def get_messages(state):
    """Return conversation history."""
    return state.get("messages", [])


def add_user_message(state, message):
    """Store a user message."""
    messages = get_messages(state)
    messages.append(HumanMessage(content=message))
    state["messages"] = messages
    return state


def add_ai_message(state, message):
    """Store an AI message."""
    messages = get_messages(state)
    messages.append(AIMessage(content=message))
    state["messages"] = messages
    return state


def clear_messages(state):
    """Clear conversation history."""
    state["messages"] = []
    return state


# ==========================
# Session Memory
# ==========================

def get_session(state):
    """
    Return the current session.
    Placeholder for future Redis/Database.
    """
    return state


# ==========================
# Long-Term Memory
# ==========================

def load_long_term_memory(user_id=None):
    """
    Placeholder for future Vector DB / SQL.
    """
    return []


def save_long_term_memory(user_id=None, memory=None):
    """
    Placeholder for future Vector DB / SQL.
    """
    return