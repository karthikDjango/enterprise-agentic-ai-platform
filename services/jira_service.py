import re

from tools.jira.jira_tool import JiraTool

jira_tool = JiraTool()


def get_project_issues():
    return jira_tool.get_project_issues("EAI")


def get_issue(issue_key: str):
    return jira_tool.get_issue(issue_key)


def create_issue(summary: str):
    return jira_tool.create_issue(
        project_key="EAI",
        summary=summary,
        description=summary,
    )


def _handle_list_issues() -> str:
    data = get_project_issues()

    issues = data.get("issues", [])

    if not issues:
        return "No Jira issues found."

    response = []

    for issue in issues:
        response.append(
            f"{issue['key']} - {issue['fields']['summary']}"
        )

    return "\n".join(response)


def _handle_get_issue(issue_key: str) -> str:
    issue = get_issue(issue_key)

    return (
        f"Key      : {issue['key']}\n"
        f"Summary  : {issue['fields']['summary']}\n"
        f"Status   : {issue['fields']['status']['name']}\n"
        f"Type     : {issue['fields']['issuetype']['name']}"
    )


def _handle_create_issue(question: str) -> str:
    
    summary = (
        question.lower()
        .replace("create jira story", "")
        .replace("create story", "")
        .strip()
        .title()
    )

    if not summary:
        return "Please provide a story summary."

    issue = create_issue(summary)

    return (
        "✅ Jira issue created successfully.\n\n"
        f"Key: {issue['key']}"
    )


def handle_jira_request(question: str) -> str:
    print("✅ Jira Service")
    question = question.strip().lower()

    if question.startswith("create jira story"):
        
        return _handle_create_issue(question)

    match = re.search(r"[A-Z]+-\d+", question.upper())

    if match:
        
        return _handle_get_issue(match.group())

    print(">>> LIST ISSUES PATH")
    return _handle_list_issues()