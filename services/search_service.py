from config import tavily_client


def search(query: str) -> dict:
    """
    Perform a web search using Tavily.
    """

    try:
        response = tavily_client.search(
            query=query,
            max_results=5,
        )

        return {
            "success": True,
            "provider": "tavily",
            "results": response.get("results", []),
        }

    except Exception as e:
        print(f"Tavily Error: {e}")

        return {
            "success": False,
            "provider": "tavily",
            "results": [],
        }