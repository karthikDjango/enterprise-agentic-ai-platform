import requests

from config import (
    GITHUB_TOKEN,
    GITHUB_OWNER,
    GITHUB_REPOSITORY,
)


class GitHubTool:
    """
    GitHub REST API Client

    Responsibility:
    - Authenticate with GitHub
    - Execute HTTP requests
    - Return JSON responses

    No business logic belongs here.
    """

    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get_repository(self) -> dict:
        """
        Get repository information.
        """

        url = (
            f"{self.BASE_URL}/repos/"
            f"{GITHUB_OWNER}/{GITHUB_REPOSITORY}"
        )

        response = requests.get(
            url=url,
            headers=self.headers,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()