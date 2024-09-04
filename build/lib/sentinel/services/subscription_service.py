from sentinel.config import Config

class SubscriptionService:
    def __init__(self):
        self.subscriptions = Config.get_subscribed_repositories()

    def add_subscription(self, repo):
        if repo not in self.subscriptions:
            self.subscriptions.append(repo)
            self.save_subscriptions()

    def remove_subscription(self, repo):
        if repo in self.subscriptions:
            self.subscriptions.remove(repo)
            self.save_subscriptions()

    def list_subscriptions(self):
        return self.subscriptions

    def save_subscriptions(self):
        # 将当前订阅的仓库写回 JSON 文件
        with open("subscriptions.json", "w") as file:
            json.dump({"repositories": self.subscriptions}, file, indent=4)
