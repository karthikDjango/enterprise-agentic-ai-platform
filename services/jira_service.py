from tools.jira.jira_tool import JiraTool


jira_tool = JiraTool()


def handle_jira_request(question: str) -> str:
    print("✅ Jira Service")

    data = jira_tool.get_project_issues("EAI")

    issues = data.get("issues", [])

    if not issues:
        return "No Jira issues found."

    response = []

    for issue in issues:
        key = issue["key"]
        summary = issue["fields"]["summary"]

        response.append(f"{key} - {summary}")

    return "\n".join(response)