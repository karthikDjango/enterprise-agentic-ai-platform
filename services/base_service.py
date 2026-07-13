from abc import ABC, abstractmethod

from models.enterprise_request import EnterpriseRequest


class BaseService(ABC):
    """
    Base interface for all enterprise services.
    """

    @abstractmethod
    def execute(self, request: EnterpriseRequest) -> str:
        pass