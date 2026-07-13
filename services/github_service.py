print(">>> Loaded github_service.py")

import os
print(os.path.abspath(__file__))

from models.enterprise_request import EnterpriseRequest
from services.base_service import BaseService
from tools.github.github_tool import GitHubTool


class GitHubService(BaseService):
    """
    GitHub Business Service

    Responsibilities
    ----------------
    - Business logic
    - Data transformation
    - Validation
    - Execute EnterpriseRequest

    Does NOT:
    - Understand natural language
    - Know about LangGraph
    """

    def __init__(self):
        print(">>> GitHubService initialized")
        self.github_tool = GitHubTool()

    def execute(self, request: EnterpriseRequest) -> str:
        """
        Execute GitHub operations from a structured EnterpriseRequest.
        """

        print("✅ GitHub Service")

        operation = request.operation

        if operation == "repository_details":
            return self._handle_repository_details()

        if operation == "list_repositories":
            return self._handle_list_repositories()

        return f"Unsupported GitHub operation: {operation}"

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def get_repository_details(self) -> dict:
        """
        Returns repository details.
        """

        repository = self.github_tool.get_repository()

        return {
            "name": repository["name"],
            "full_name": repository["full_name"],
            "description": repository["description"],
            "default_branch": repository["default_branch"],
            "language": repository["language"],
            "visibility": repository["visibility"],
            "stars": repository["stargazers_count"],
            "forks": repository["forks_count"],
            "open_issues": repository["open_issues_count"],
            "url": repository["html_url"],
        }

    # ---------------------------------------------------------
    # Internal handlers
    # ---------------------------------------------------------

    def _handle_repository_details(self) -> str:
        repository = self.get_repository_details()

        return (
            f"Repository: {repository['full_name']}\n"
            f"Description: {repository['description']}\n"
            f"Language: {repository['language']}\n"
            f"Stars: {repository['stars']}\n"
            f"Open Issues: {repository['open_issues']}\n"
            f"Default Branch: {repository['default_branch']}\n"
            f"URL: {repository['url']}"
        )

    def _handle_list_repositories(self) -> str:
        """
        Temporary implementation.

        We currently support one repository.
        Later this will call GitHub's list repositories API.
        """

        return self._handle_repository_details()
    
    print("Methods in GitHubService:")
    print([m for m in dir(GitHubService) if not m.startswith("__")])