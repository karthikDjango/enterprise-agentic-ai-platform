import requests
from requests.auth import HTTPBasicAuth

from config import (
    JIRA_BASE_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN,
)


class JiraTool:
    """
    Jira REST API Client

    Responsibility:
    - Authenticate with Jira
    - Execute HTTP requests
    - Return JSON responses

    No business logic belongs here.
    """

    def __init__(self):
        self.auth = HTTPBasicAuth(
            JIRA_EMAIL,
            JIRA_API_TOKEN,
        )

        self.headers = {
            "Accept": "application/json",
        }

    def get_project_issues(self, project_key: str) -> dict:
        """
        Get issues from a Jira project.
        """

        url = f"{JIRA_BASE_URL}/rest/api/3/search/jql"

        params = {
            "jql": f"project = {project_key} ORDER BY created DESC",
            "maxResults": 10,
            "fields": "summary,status,assignee",
        }

        response = requests.get(
            url=url,
            headers=self.headers,
            auth=self.auth,
            params=params,
            timeout=30,
        )

        print("URL:", response.url)
        print("Status:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))
        print("First 500 chars:")
        print(response.text[:500])

        response.raise_for_status()
        return response.json()