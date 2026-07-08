from tools.github.github_tool import GitHubTool


class GitHubService:
    """
    GitHub Business Service

    Responsibility:
    - Business logic
    - Data transformation
    - Validation

    This layer should not know anything
    about LangGraph.
    """

    def __init__(self):
        self.github_tool = GitHubTool()

    def get_repository_details(self) -> dict:
        """
        Returns only the repository information
        needed by the application.
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