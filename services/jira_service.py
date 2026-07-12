import re
from tools.jira.jira_tool import JiraTool


jira_tool = JiraTool()


def get_project_issues():
    """
    Get the latest issues from the EAI project.
    """
    return jira_tool.get_project_issues("EAI")


def get_issue(issue_key: str):
    """
    Get a single Jira issue.
    """
    return jira_tool.get_issue(issue_key)


def handle_jira_request(question: str) -> str:
    print("✅ Jira Service")

    # Look for a Jira issue key like EAI-6
    match = re.search(r"[A-Z]+-\d+", question.upper())

    if match:
        issue_key = match.group()

        issue = get_issue(issue_key)

        return (
            f"Key      : {issue['key']}\n"
            f"Summary  : {issue['fields']['summary']}\n"
            f"Status   : {issue['fields']['status']['name']}\n"
            f"Type     : {issue['fields']['issuetype']['name']}"
        )

    data = get_project_issues()

    issues = data.get("issues", [])

    if not issues:
        return "No Jira issues found."

    response = []

    for issue in issues:
        key = issue["key"]
        summary = issue["fields"]["summary"]

        response.append(f"{key} - {summary}")

    return "\n".join(response)