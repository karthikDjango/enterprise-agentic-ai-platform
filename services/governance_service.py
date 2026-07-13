from models.enterprise_request import EnterpriseRequest
from models.governance_decision import GovernanceDecision


class GovernanceService:
    """
    Enterprise AI Governance Service

    Responsibilities
    ----------------
    - Evaluate enterprise policies
    - Classify request risk
    - Decide whether execution is allowed

    Does NOT:
    - Execute APIs
    - Route requests
    - Modify requests
    """

    def evaluate(
        self,
        request: EnterpriseRequest,
    ) -> GovernanceDecision:

        operation = request.operation.lower().strip()

        # ----------------------------
        # Read Operations
        # ----------------------------
        if operation in (
            "list",
            "list_issues",
            "get",
            "get_issue",
            "search",
            "search_issues",
            "list_repositories",
            "get_repository",
        ):
            return GovernanceDecision(
                allowed=True,
                risk="LOW",
                reason="Read operation permitted."
            )

        # ----------------------------
        # Create Operations
        # ----------------------------
        if operation in (
            "create",
            "create_issue",
            "create_repository",
        ):
            return GovernanceDecision(
                allowed=True,
                risk="MEDIUM",
                reason="Create operation permitted."
            )

        # ----------------------------
        # Update Operations
        # ----------------------------
        if operation in (
            "update",
            "update_issue",
            "update_repository",
        ):
            return GovernanceDecision(
                allowed=True,
                risk="HIGH",
                reason="Update operation requires elevated monitoring."
            )

        # ----------------------------
        # Delete Operations
        # ----------------------------
        if operation in (
            "delete",
            "delete_issue",
            "delete_repository",
        ):
            return GovernanceDecision(
                allowed=False,
                risk="CRITICAL",
                reason="Delete operations are blocked by enterprise policy."
            )

        # ----------------------------
        # Unknown Operations
        # ----------------------------
        return GovernanceDecision(
            allowed=False,
            risk="HIGH",
            reason=f"Unknown operation '{operation}'."
        )