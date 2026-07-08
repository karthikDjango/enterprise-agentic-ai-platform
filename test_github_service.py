from services.github_service import GitHubService


service = GitHubService()

repository = service.get_repository_details()

for key, value in repository.items():
    print(f"{key}: {value}")