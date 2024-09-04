import requests
from sentinel.config import Config

class GitHubAPI:
    def __init__(self):
        self.token = Config.GITHUB_TOKEN
        self.headers = {'Authorization': f'token {self.token}'}

    def get_repo_updates(self, repo):
        url = f'https://api.github.com/repos/{repo}/commits'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_latest_release(self, repo):
        url = f'https://api.github.com/repos/{repo}/releases/latest'
        response = requests.get(url, headers=self.headers)
        return response.json()




