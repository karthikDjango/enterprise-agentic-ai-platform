from typing import Any

from pydantic import BaseModel


class EnterpriseRequest(BaseModel):
    tool: str
    operation: str
    parameters: dict[str, Any]
    confidence: float = 1.0