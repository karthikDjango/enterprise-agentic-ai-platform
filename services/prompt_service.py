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


def get_parameter_extraction_prompt(user_query: str):
    """
    Prompt used to convert natural language into a structured EnterpriseRequest.
    """

    return f"""
You are an Enterprise AI parameter extraction engine.

Your job is to convert the user's request into a structured EnterpriseRequest.

Return ONLY valid JSON.

JSON Schema:

{{
    "tool": "<tool name>",
    "operation": "<operation>",
    "parameters": {{
    }},
    "confidence": 1.0
}}

Rules:

1. Return ONLY JSON.
2. Do NOT explain your answer.
3. Do NOT use markdown.
4. Do NOT wrap the JSON inside triple backticks.
5. Extract every parameter you can identify.
6. If a parameter is missing, leave it empty.
7. Use lowercase values for tool and operation.

Supported tools:

- jira
- github

Supported Jira operations:

- list_issues
- get_issue
- create_issue

Supported GitHub operations:

- list_repositories
- repository_details

Examples:

User:
Create Jira story Redis caching

Output:
{{
    "tool": "jira",
    "operation": "create_issue",
    "parameters": {{
        "issue_type": "Story",
        "summary": "Redis caching"
    }},
    "confidence": 0.99
}}

User:
Show Jira issue EAI-6

Output:
{{
    "tool": "jira",
    "operation": "get_issue",
    "parameters": {{
        "issue_key": "EAI-6"
    }},
    "confidence": 0.99
}}

User:
List Jira issues

Output:
{{
    "tool": "jira",
    "operation": "list_issues",
    "parameters": {{}},
    "confidence": 0.99
}}

User:
Show my GitHub repositories

Output:
{{
    "tool": "github",
    "operation": "list_repositories",
    "parameters": {{}},
    "confidence": 0.99
}}

User:
Show repository enterprise-agentic-ai-platform

Output:
{{
    "tool": "github",
    "operation": "repository_details",
    "parameters": {{
        "repository": "enterprise-agentic-ai-platform"
    }},
    "confidence": 0.99
}}

User:
{user_query}
"""