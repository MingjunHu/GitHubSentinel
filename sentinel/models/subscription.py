class Subscription:
    def __init__(self, repo):
            self.repo = repo
	    EOF

	    cat <<EOF > GitHubSentinel/sentinel/models/update.py
	    class Update:
	        def __init__(self, data):
		        self.data = data
			EOF

			cat <<EOF > GitHubSentinel/sentinel/services/subscription_service.py
			from sentinel.models.subscription import Subscription

			class SubscriptionService:
			    def __init__(self):
			            self.subscriptions = []

    def add_subscription(self, repo):
        sub = Subscription(repo)
        self.subscriptions.append(sub)

    def remove_subscription(self, repo):
        self.subscriptions = [sub for sub in self.subscriptions if sub.repo != repo]

    def list_subscriptions(self):
        return [sub.repo for sub in self.subscriptions]
