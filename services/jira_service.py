from models.enterprise_request import EnterpriseRequest
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


def _handle_create_issue(request: EnterpriseRequest) -> str:
    summary = request.parameters.get("summary")

    if not summary:
        return "Please provide a story summary."

    issue = create_issue(summary)

    return (
        "✅ Jira issue created successfully.\n\n"
        f"Key: {issue['key']}"
    )


def handle_jira_request(request: EnterpriseRequest) -> str:
    """
    Execute Jira operations from a structured EnterpriseRequest.
    """

    print("✅ Jira Service")

    operation = request.operation

    if operation == "create_issue":
        return _handle_create_issue(request)

    if operation == "get_issue":
        issue_key = request.parameters.get("issue_key")

        if not issue_key:
            return "Issue key is missing."

        return _handle_get_issue(issue_key)

    if operation == "list_issues":
        return _handle_list_issues()

    return f"Unsupported Jira operation: {operation}"