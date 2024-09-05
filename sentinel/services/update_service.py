from sentinel.utils.github_api import GitHubAPI

class UpdateService:
    def __init__(self, repo):
        self.repo = repo
        self.github_api = GitHubAPI()

    def check_updates(self):
        try:
            issues = self.github_api.get_repo_issues(self.repo)
            pulls = self.github_api.get_repo_pull_requests(self.repo)
            commits = self.github_api.get_repo_commits(self.repo)

            updates = {
                "issues": issues,
                "pulls": pulls,
                "commits": commits
            }

            return updates
        except Exception as e:
            print(f"Error fetching updates for {self.repo}: {e}")
            return None
