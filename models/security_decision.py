from pydantic import BaseModel


class SecurityDecision(BaseModel):
    """
    Represents the AI security evaluation of a user prompt.
    """

    allowed: bool
    risk: str
    reason: str