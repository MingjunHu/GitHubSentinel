# sentinel/utils/github_api.py

import requests
from datetime import datetime
import os
from sentinel.config import Config

class GitHubAPI:
    def __init__(self):
        self.token = Config.GITHUB_TOKEN
        self.headers = {'Authorization': f'token {self.token}'}

    def get_repo_issues(self, repo):
        url = f'https://api.github.com/repos/{repo}/issues'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_repo_pull_requests(self, repo):
        url = f'https://api.github.com/repos/{repo}/pulls'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_repo_commits(self, repo):
        url = f'https://api.github.com/repos/{repo}/commits'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def export_to_markdown(self, repo, issues, pulls, commits):
        # 创建以 repo 和当前日期命名的 markdown 文件
        date = datetime.now().strftime('%Y-%m-%d')
        filename = f"{repo.replace('/', '_')}_{date}.md"
        filepath = os.path.join('daily_reports', filename)
        os.makedirs('daily_reports', exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# Daily Progress for {repo} - {date}\n\n")

            # Issues
            md_file.write("## Issues:\n")
            if issues:
                for issue in issues:
                    md_file.write(f"- [{issue['title']}]({issue['html_url']})\n")
            else:
                md_file.write("No issues found.\n")
            md_file.write("\n")

            # Pull Requests
            md_file.write("## Pull Requests:\n")
            if pulls:
                for pull in pulls:
                    md_file.write(f"- [{pull['title']}]({pull['html_url']})\n")
            else:
                md_file.write("No pull requests found.\n")
            md_file.write("\n")

            # Commits
            md_file.write("## Commits:\n")
            if commits:
                for commit in commits:
                    commit_message = commit['commit']['message'].split('\n')[0]  # 只取第一行
                    commit_url = commit['html_url']
                    md_file.write(f"- [{commit_message}]({commit_url})\n")
            else:
                md_file.write("No commits found.\n")
        
        print(f"Exported daily report to {filepath}")
        return filepath
