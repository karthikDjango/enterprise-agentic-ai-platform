"""
Enterprise Tool Dispatcher

Responsibility:
- Decide which enterprise tool should execute the request.
- Return the execution node name.

This module does NOT execute tools.
"""


class EnterpriseDispatcher:

    def dispatch(self, question: str) -> str:
        question = question.lower()

        github_keywords = [
            "github",
            "repository",
            "repo",
            "pull request",
            "pr",
            "commit",
            "branch",
            "issue",
        ]

        jira_keywords = [
            "jira",
            "story",
            "epic",
            "sprint",
            "backlog",
            "ticket",
        ]

        email_keywords = [
            "email",
            "mail",
            "outlook",
            "gmail",
        ]

        calendar_keywords = [
            "calendar",
            "meeting",
            "schedule",
            "appointment",
            "event",
        ]

        if any(word in question for word in github_keywords):
            return "github"

        if any(word in question for word in jira_keywords):
            return "jira"

        if any(word in question for word in email_keywords):
            return "email"

        if any(word in question for word in calendar_keywords):
            return "calendar"

        return "unknown"