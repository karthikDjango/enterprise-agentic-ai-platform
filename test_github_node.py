from nodes.execution.github_node import github_node


state = {
    "question": "Tell me about my repository",
    "response": "",
    "intent": "github",
    "tool_used": "",
    "messages": [],
    "session_id": "test-session",
}

result = github_node(state)

print(result["response"])
print(result["tool_used"])