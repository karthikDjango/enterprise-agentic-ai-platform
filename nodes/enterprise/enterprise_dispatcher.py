from models.enterprise_request import EnterpriseRequest


class EnterpriseDispatcher:
    """
    Enterprise Dispatcher

    Responsibility:
    - Receive a validated EnterpriseRequest
    - Decide which enterprise tool should execute it

    Does NOT:
    - Parse English
    - Use regex
    - Perform keyword matching
    - Execute tools
    """

    def dispatch(self, request: EnterpriseRequest) -> str:
        return request.tool