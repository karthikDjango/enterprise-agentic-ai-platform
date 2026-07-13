from models.enterprise_request import EnterpriseRequest
from services.governance_service import GovernanceService

request = EnterpriseRequest(
    tool="jira",
    operation="create",
    parameters={"summary": "Test Story"}
)

service = GovernanceService()
decision = service.evaluate(request)

print(decision)