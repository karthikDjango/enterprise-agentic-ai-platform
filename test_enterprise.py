from nodes.enterprise.enterprise_node import enterprise_node

state = {
    "question": "Tell me about my GitHub repository",
    "response": "",
    "intent": "enterprise",
    "tool_used": "",
    "messages": [],
    "session_id": "test-session",
}

result = enterprise_node(state)

print("\n--------------------------")
print(result["response"])
print("--------------------------")
print("Tool Used:", result["tool_used"])