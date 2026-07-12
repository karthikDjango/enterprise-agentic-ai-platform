import re


class EnterpriseDispatcher:

    def dispatch(self, question: str) -> str:
       
        question = question.lower()

        # Detect Jira issue keys like EAI-6
        if re.search(r"[a-z]+-\d+", question):
            
            return "jira"

        github_keywords = [
            "github",
            "repository",
            "repositories",
            "repo",
            "repos",
            "pull request",
            "pr",
            "commit",
            "branch",
        ]

        jira_keywords = [
            "jira",
            "ticket",
            "tickets",
            "story",
            "stories",
            "epic",
            "sprint",
            "backlog",
        ]

        if any(word in question for word in jira_keywords):
            return "jira"

        if any(word in question for word in github_keywords):
            return "github"

        
        return "unknown"