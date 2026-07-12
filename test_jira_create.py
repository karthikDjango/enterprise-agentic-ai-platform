from tools.jira.jira_tool import JiraTool


def main():
    jira = JiraTool()

    response = jira.create_issue(
        project_key="EAI",
        summary="Implement Redis caching",
        description="Create Redis caching layer for Enterprise Agentic AI Platform.",
    )

    print("\n✅ Jira Issue Created\n")
    print(response)


if __name__ == "__main__":
    main()