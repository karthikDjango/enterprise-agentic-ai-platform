import json

from pydantic import ValidationError

from models.enterprise_request import EnterpriseRequest
from services.llm_service import ask_gemini_prompt
from services.prompt_service import get_parameter_extraction_prompt


class ParameterExtractionService:
    """
    Converts natural language into a validated EnterpriseRequest.

    Responsibilities:
    - Build the extraction prompt
    - Call Gemini
    - Parse JSON
    - Validate against EnterpriseRequest
    - Return a structured EnterpriseRequest

    Does NOT:
    - Execute tools
    - Call Jira or GitHub APIs
    - Make routing decisions
    """

    def extract(self, user_input: str) -> EnterpriseRequest:
        """
        Extract structured enterprise parameters from natural language.
        """

        prompt = get_parameter_extraction_prompt(user_input)

        print("\n===== PARAMETER EXTRACTION PROMPT =====")
        print(prompt)

        response = ask_gemini_prompt(prompt)

        print("\n===== GEMINI RESPONSE =====")
        print(response)

        try:
            data = json.loads(response)

            request = EnterpriseRequest.model_validate(data)

            return request

        except json.JSONDecodeError as e:
            raise ValueError(
                f"Gemini returned invalid JSON.\n\nResponse:\n{response}"
            ) from e

        except ValidationError as e:
            raise ValueError(
                f"Gemini returned invalid EnterpriseRequest.\n\n{e}"
            ) from e