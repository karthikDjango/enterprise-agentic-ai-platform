from models.security_decision import SecurityDecision


class AISecurityService:
    """
    Evaluates whether a user prompt is safe to process.
    """

    BLOCKED_PATTERNS = [
        # Prompt injection
        "ignore previous instructions",
        "forget previous instructions",
        "override instructions",

        # Jailbreak
        "developer mode",
        "unrestricted mode",
        "you are no longer",

        # Secret extraction
        "api key",
        "password",
        "token",
        "system prompt",
        "environment variables",

        # Dangerous commands
        "rm -rf",
        "drop database",
        "delete everything",
        "shutdown server",
    ]

    def evaluate(self, question: str) -> SecurityDecision:
        """
        Evaluate whether a prompt is safe.
        """

        text = question.lower()

        for pattern in self.BLOCKED_PATTERNS:
            if pattern in text:
                return SecurityDecision(
                    allowed=False,
                    risk="CRITICAL",
                    reason=f"Blocked pattern detected: '{pattern}'"
                )

        return SecurityDecision(
            allowed=True,
            risk="LOW",
            reason="Prompt is safe."
        )