# 生成更新报告的模块
# 此处可以实现将从 GitHub 获取的更新信息整理并格式化为报告的功能

from sentinel.utils.github_api import GitHubAPI

def generate_report():
    report = fetch_langchain_latest_release()
    with open("langchain_latest_release_report.txt", "w") as file:
        file.write(report)

    return report



def fetch_langchain_latest_release():
    github_api = GitHubAPI()
    latest_release = github_api.get_latest_release('langchain-ai/langchain')
                
    if latest_release:
        report = f"""
        Latest Release Information for langchain:
        - Tag: {latest_release['tag_name']}
        - Name: {latest_release['name']}
        - Published at: {latest_release['published_at']}
        - Body: {latest_release['body']}
        """
        return report
    else:
        return "No latest release found for langchain."





if __name__ == "__main__":
    print(generate_report())
