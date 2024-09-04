from sentinel.utils.github_api import GitHubAPI

class UpdateService:
    def __init__(self, repo):
        self.repo = repo
        self.github_api = GitHubAPI()

    def check_updates(self):
        updates = self.github_api.get_repo_updates(self.repo)
        return updates
