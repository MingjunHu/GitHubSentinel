import time
from sentinel.services.update_service import UpdateService
from sentinel.services.notification_service import NotificationService
from sentinel.config import Config

class Scheduler:
    def __init__(self, subscription_service):
        self.subscription_service = subscription_service
        self.notification_service = NotificationService()
        self._running = True  # 新增一个标志来控制后台运行

    def start(self):
        while self._running:
            for repo in self.subscription_service.list_subscriptions():
                update_service = UpdateService(repo)
                updates = update_service.check_updates()
                if updates:
                    self.notification_service.send_email(f"Updates for {repo}", str(updates))
            # 根据配置设置检查频率
            time.sleep(86400 if Config.UPDATE_FREQUENCY == 'daily' else 604800)

    def stop(self):
        print("Stopping Scheduler...")
        self._running = False
