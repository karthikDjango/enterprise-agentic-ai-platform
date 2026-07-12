from services.jira_service import get_issue


def main():
    issue = get_issue("EAI-6")

    print("\n✅ Jira Service Test\n")

    print(f"Key      : {issue['key']}")
    print(f"Summary  : {issue['fields']['summary']}")
    print(f"Status   : {issue['fields']['status']['name']}")
    print(f"Type     : {issue['fields']['issuetype']['name']}")


if __name__ == "__main__":
    main()