#sentinel/daemon_process.py

import schedule # 导入 schedule 实现定时任务执行器
import time  # 导入time库，用于控制时间间隔
import signal  # 导入signal库，用于信号处理
import sys  # 导入sys库，用于执行系统相关的操作
import os   # 导入os模块用于文件和目录操作
from datetime import datetime,timedelta  # 导入 datetime 模块用于获取当前日期

from sentinel.config import Config
from sentinel.daily_progress import generate_daily_progress
from sentinel.report_generator import ReportGenerator
from sentinel.tasks.scheduler import Scheduler
from sentinel.services.subscription_service import SubscriptionService
from sentinel.services.notification_service import NotificationService
from sentinel.utils.github_api import GitHubAPI
from sentinel.logger import LOG  # 导入日志模块
from sentinel.llm_module import LLMModule
from sentinel.utils.hacker_news_api import HackerNewsClient


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
        markdown_file_path =github_api.export_to_markdown_by_date_range(repo,days)
        #生成进展报告
        report, report_file_path=report_generator.generate_formal_report(markdown_file_path)
        #发送email
        notification_service.send_email(f"[GitHubSentinel]{repo} 进展简报", report)
    LOG.info(f"[定时任务执行完毕]")

def hn_topic_job(hacker_news_client, report_generator):
    LOG.info("[开始执行定时任务]Hacker News 热点话题跟踪")
    markdown_file_path = hacker_news_client.export_top_stories()
    _, _ = report_generator.generate_hn_topic_report(markdown_file_path)
    LOG.info(f"[定时任务执行完毕]")

def hn_daily_job(hacker_news_client, report_generator, notification_service):
    LOG.info("[开始执行定时任务]Hacker News 今日前沿技术趋势")
    # 获取前一日的日期，并格式化为 'YYYY-MM-DD' 格式
    # 获取当前日期和时间
    now = datetime.now()

    # 计算日期
    the_data = now - timedelta(days=1)

    # 格式化日期（可选）
    date = the_data.strftime('%Y-%m-%d')

    # 生成每日汇总报告的目录路径
    directory_path = os.path.join('hacker_news', date)
    # 确保目录存在
    os.makedirs(directory_path, exist_ok=True) 
    # 生成每日汇总报告并保存
    report, _ = report_generator.generate_hn_daily_report(directory_path)
    notification_service.send_email(f"[HackerNews] {date} 技术趋势", report)
    LOG.info(f"[定时任务执行完毕]")


def main():
    # 设置信号处理器
    signal.signal(signal.SIGTERM, graceful_shutdown)

    config = Config()  # 创建配置实例
    subscription_service = SubscriptionService()
    notification_service = NotificationService()
    github_api=GitHubAPI()
    hacker_news_client = HackerNewsClient() # 创建 Hacker News 客户端实例
    llm = LLMModule(config)  # 创建语言模型实例
    report_generator=ReportGenerator(llm, config.report_types)

    # 启动时立即执行（如不需要可注释）
    github_job(subscription_service, github_api, report_generator, notification_service, config.freq_days)
    hn_daily_job(hacker_news_client, report_generator, notification_service)
    
    # 安排每天的定时任务
    schedule.every(config.freq_days).days.at(
        config.exec_time
    ).do(github_job, subscription_service, github_api, report_generator, notification_service, config.freq_days)

    # 安排 hn_topic_job 每4小时执行一次，从0点开始
    schedule.every(4).hours.at(":00").do(hn_topic_job, hacker_news_client, report_generator)

    # 安排 hn_daily_job 每天早上10点执行一次
    schedule.every().day.at("05:00").do(hn_daily_job, hacker_news_client, report_generator, notification_service)

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