#/sentinel/tasks/scheduler.py

import time
import daemon
from sentinel.services.update_service import UpdateService
from sentinel.config import Config
from sentinel.utils.github_api import GitHubAPI
from sentinel.report_generator import ReportGenerator
from sentinel.logger import LOG

class Scheduler:
    def __init__(self, subscription_service,report_generator,github_api,notification_service,_running):
        self.subscription_service = subscription_service
        self.notification_service = notification_service
        self.github_api=github_api
        self.report_generator=report_generator
        self._running = _running  # 用于控制后台运行的标志

    def start(self):
        # 使用python-daemon库，以守护进程方式运行程序
        #with daemon.DaemonContext():
        while self._running:
            for repo in self.subscription_service.list_subscriptions():
                # try:
                #     #update_service = UpdateService(repo)
                #     updates = update_service.check_updates()
                #     if updates and (updates['issues'] or updates['pulls'] or updates['commits']):
                #         # 将更新信息格式化并发送通知
                #         update_message = (
                #             f"Issues: {len(updates['issues'])}, "
                #             f"Pull Requests: {len(updates['pulls'])}, "
                #             f"Commits: {len(updates['commits'])}"
                #         )
                #         self.notification_service.send_email(f"Updates for {repo}", update_message)
                # except Exception as e:
                #     print(f"Error updating repository {repo}: {e}")
                markdown_file_path =self.github_api.export_to_markdown(repo)
                report, report_file_path=self.report_generator.generate_formal_report(markdown_file_path)
                self.notification_service.send_email(f"{repo} 项目进展 by GitHubSentinel", report)
                time.sleep(1)
            # 根据配置设置检查频率
            #time.sleep(86400 if Config.UPDATE_FREQUENCY == 'daily' else 604800)
            time.sleep(180)#测试用3分钟

    def stop(self):
        print("Stopping Scheduler...")
        self._running = False
