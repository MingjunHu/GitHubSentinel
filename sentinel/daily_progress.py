# sentinel/daily_progress.py
import requests
from sentinel.utils.github_api import GitHubAPI
from sentinel.config import Config

def generate_daily_progress():
    github_api = GitHubAPI()
    for repo in Config.get_subscribed_repositories():
        try:
            #issues = github_api.get_repo_issues(repo)
            #pulls = github_api.get_repo_pull_requests(repo)
            #commits = github_api.get_repo_commits(repo)
            github_api.export_to_markdown(repo)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {repo}: {e}")

if __name__ == "__main__":
    generate_daily_progress()
