from services.parameter_extraction_service import ParameterExtractionService

service = ParameterExtractionService()

queries = [
    "Create Jira story Redis caching",
    "Show Jira issue EAI-6",
    "List Jira issues",
    "Show my GitHub repositories",
]

for query in queries:
    print("=" * 60)
    print(f"User: {query}")

    try:
        request = service.extract(query)

        print("\nEnterpriseRequest:")
        print(request)

        print("\nAs Dictionary:")
        print(request.model_dump())

    except Exception as e:
        print(e)