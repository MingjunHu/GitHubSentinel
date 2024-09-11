#sentinel/daemon_process.py

import schedule # 导入 schedule 实现定时任务执行器
import time  # 导入time库，用于控制时间间隔
import signal  # 导入signal库，用于信号处理
import sys  # 导入sys库，用于执行系统相关的操作

from sentinel.config import Config
from sentinel.daily_progress import generate_daily_progress
from sentinel.report_generator import ReportGenerator
from sentinel.tasks.scheduler import Scheduler
from sentinel.services.subscription_service import SubscriptionService
from sentinel.services.notification_service import NotificationService
from sentinel.utils.github_api import GitHubAPI
from sentinel.logger import LOG  # 导入日志模块


def graceful_shutdown(signum, frame):
    # 优雅关闭程序的函数，处理信号时调用
    LOG.info("[优雅退出]守护进程接收到终止信号")
    sys.exit(0)  # 安全退出程序

def graceful_shutdown(signum, frame):
    # 优雅关闭程序的函数，处理信号时调用
    LOG.info("[优雅退出]守护进程接收到终止信号")
    sys.exit(0)  # 安全退出程序

def github_job(subscription_service, github_api, report_generator, notification_service, days):
    LOG.info("[开始执行定时任务]")
    subscriptions = subscription_service.list_subscriptions()  # 获取当前所有订阅
    LOG.info(f"订阅列表：{subscriptions}")
    for repo in subscriptions:
        #获取进展信息
        markdown_file_path =github_api.export_to_markdown(repo)
        #生成进展报告
        report, report_file_path=report_generator.generate_formal_report(markdown_file_path)
        #发送email
        notification_service.send_email(f"[GitHubSentinel]{repo} 进展简报", report)
    LOG.info(f"[定时任务执行完毕]")


def main():
    # 设置信号处理器
    signal.signal(signal.SIGTERM, graceful_shutdown)

    config = Config()  # 创建配置实例
    subscription_service = SubscriptionService()
    notification_service = NotificationService()
    github_api=GitHubAPI()
    report_generator=ReportGenerator()

    # 启动时立即执行（如不需要可注释）
    github_job(subscription_service, github_api, report_generator, notification_service, config.freq_days)

    # 安排每天的定时任务
    schedule.every(config.freq_days).days.at(
        config.exec_time
    ).do(github_job, subscription_service, github_api, report_generator, notification_service, config.freq_days)

    try:
        # 在守护进程中持续运行
        while True:
            schedule.run_pending()
            time.sleep(1)  # 短暂休眠以减少 CPU 使用
    except Exception as e:
        LOG.error(f"主进程发生异常: {str(e)}")
        sys.exit(1)



if __name__ == '__main__':
    main()