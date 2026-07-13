from pydantic import BaseModel


class GovernanceDecision(BaseModel):
    """
    Result of enterprise governance evaluation.

    Responsibilities:
    - Indicate whether a request is allowed.
    - Classify the request risk.
    - Explain the governance decision.
    """

    allowed: bool
    risk: str
    reason: str