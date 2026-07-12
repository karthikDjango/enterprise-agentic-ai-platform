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

    def _get(self, endpoint: str, params: dict = None) -> dict:
        """
        Execute an authenticated HTTP GET request.
        """

        url = f"{JIRA_BASE_URL}{endpoint}"

        response = requests.get(
            url=url,
            headers=self.headers,
            auth=self.auth,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    def _post(self, endpoint: str, data: dict = None) -> dict:
        """
        Execute an authenticated HTTP POST request.
        """

        url = f"{JIRA_BASE_URL}{endpoint}"

        response = requests.post(
            url=url,
            headers=self.headers,
            auth=self.auth,
            json=data,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    def _put(self, endpoint: str, data: dict = None) -> dict:
        """
        Execute an authenticated HTTP PUT request.
        """

        url = f"{JIRA_BASE_URL}{endpoint}"

        response = requests.put(
            url=url,
            headers=self.headers,
            auth=self.auth,
            json=data,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    def get_project_issues(self, project_key: str) -> dict:
        """
        Get issues from a Jira project.
        """

        params = {
            "jql": f"project = {project_key} ORDER BY created DESC",
            "maxResults": 10,
            "fields": "summary,status,assignee",
        }

        return self._get(
            endpoint="/rest/api/3/search/jql",
            params=params,
        )
    def get_issue(self, issue_key: str) -> dict:
        """
         Get a single Jira issue.
        """

        return self._get(
        endpoint=f"/rest/api/3/issue/{issue_key}",
        )
    def create_issue(
        self,
        project_key: str,
        summary: str,
        description: str,
        issue_type: str = "Story",
    ) -> dict:
        """
        Create a Jira issue.
        """

        data = {
            "fields": {
                "project": {
                    "key": project_key,
                },
                "summary": summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": description,
                                }
                            ],
                        }
                    ],
                },
                "issuetype": {
                    "name": issue_type,
                },
            }
        }

        return self._post(
            endpoint="/rest/api/3/issue",
            data=data,
        )