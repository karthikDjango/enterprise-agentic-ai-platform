from models.enterprise_request import EnterpriseRequest
from services.base_service import BaseService
from tools.jira.jira_tool import JiraTool


class JiraService(BaseService):
    """
    Jira Business Service

    Responsibilities
    ----------------
    - Business logic
    - Validation
    - Data transformation
    - Execute EnterpriseRequest

    Does NOT:
    - Understand natural language
    - Know about LangGraph
    """

    def __init__(self):
        self.jira_tool = JiraTool()

    def execute(self, request: EnterpriseRequest) -> str:
        print("✅ Jira Service")

        operation = request.operation

        if operation == "create_issue":
            return self._handle_create_issue(request)

        if operation == "get_issue":
            issue_key = request.parameters.get("issue_key")

            if not issue_key:
                return "Issue key is missing."

            return self._handle_get_issue(issue_key)

        if operation == "list_issues":
            return self._handle_list_issues()

        return f"Unsupported Jira operation: {operation}"

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def get_project_issues(self):
        return self.jira_tool.get_project_issues("EAI")

    def get_issue(self, issue_key: str):
        return self.jira_tool.get_issue(issue_key)

    def create_issue(self, summary: str):
        return self.jira_tool.create_issue(
            project_key="EAI",
            summary=summary,
            description=summary,
        )

    # ---------------------------------------------------------
    # Internal handlers
    # ---------------------------------------------------------

    def _handle_list_issues(self) -> str:
        data = self.get_project_issues()

        issues = data.get("issues", [])

        if not issues:
            return "No Jira issues found."

        response = []

        for issue in issues:
            response.append(
                f"{issue['key']} - {issue['fields']['summary']}"
            )

        return "\n".join(response)

    def _handle_get_issue(self, issue_key: str) -> str:
        issue = self.get_issue(issue_key)

        return (
            f"Key      : {issue['key']}\n"
            f"Summary  : {issue['fields']['summary']}\n"
            f"Status   : {issue['fields']['status']['name']}\n"
            f"Type     : {issue['fields']['issuetype']['name']}"
        )

    def _handle_create_issue(self, request: EnterpriseRequest) -> str:
        summary = request.parameters.get("summary")

        if not summary:
            return "Please provide a story summary."

        issue = self.create_issue(summary)

        return (
            "✅ Jira issue created successfully.\n\n"
            f"Key: {issue['key']}"
        )