from tools.github.github_tool import GitHubTool


tool = GitHubTool()

repo = tool.get_repository()

print("Repository :", repo["full_name"])
print("Description:", repo["description"])
print("Branch     :", repo["default_branch"])