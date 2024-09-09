#/sentinel/cli/sentinel_cli.py

import argparse
import threading
from sentinel.daily_progress import generate_daily_progress
from sentinel.report_generator import ReportGenerator
from sentinel.tasks.scheduler import Scheduler
from sentinel.services.subscription_service import SubscriptionService
from sentinel.logger import LOG  # 导入日志模块

subscription_service = SubscriptionService()
report_generator = ReportGenerator()
scheduler = None
scheduler_thread = None

def start_scheduler():
    global scheduler, scheduler_thread
    scheduler = Scheduler(subscription_service)
    scheduler_thread = threading.Thread(target=scheduler.start,args=(scheduler,))
    scheduler_thread.daemon = True  # 设置为守护线程，不阻塞主进程
    scheduler_thread.start()
    LOG.info("Scheduler thread started.")  # 记录调度器线程已启动
    
    print("Scheduler started in the background.")

def stop_scheduler():
    global scheduler
    if scheduler:
        scheduler.stop()
        print("Scheduler stopped.")
    else:
        print("No scheduler is running.")

def generate_progress():
    print("Generating daily progress...")
    generate_daily_progress()

def generate_report():
    print("Generating report from daily progress...")
    report_generator.generate_formal_reports()

def add_subscription(repo):
    subscription_service.add_subscription(repo)
    print(f"Added subscription: {repo}")

def remove_subscription(repo):
    subscription_service.remove_subscription(repo)
    print(f"Removed subscription: {repo}")

def list_subscriptions():
    print("Subscribed repositories:")
    for repo in subscription_service.list_subscriptions():
        print(f"- {repo}")

def print_help():
    help_message = """
GitHub Sentinel 命令行工具

用法:
  sentinel_cli.py progress            生成订阅项目的每日进展 Markdown 文件。
  sentinel_cli.py report              基于每日进展生成项目报告。
  sentinel_cli.py start-scheduler     在后台启动更新调度器。
  sentinel_cli.py stop-scheduler      停止后台更新调度器。
  sentinel_cli.py add <repository>    添加新的订阅仓库。
  sentinel_cli.py remove <repository> 移除订阅的仓库。
  sentinel_cli.py list                列出所有已订阅的仓库。
  sentinel_cli.py help                显示此帮助信息。

示例:
  python sentinel_cli.py progress        # 生成每日进展 Markdown 文件
  python sentinel_cli.py report          # 生成正式报告
  python sentinel_cli.py start-scheduler # 启动后台更新调度器
  python sentinel_cli.py stop-scheduler  # 停止后台更新调度器
  python sentinel_cli.py add <repository>    # 添加订阅仓库
  python sentinel_cli.py remove <repository> # 移除订阅仓库
  python sentinel_cli.py list                # 列出所有订阅的仓库
"""
    print(help_message)

def main():
    parser = argparse.ArgumentParser(prog='GitHub Sentinel', description='GitHub Sentinel Command Line Tool', add_help=True)
    
    # 定义命令
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # progress 命令：生成每日进展 Markdown 文件
    subparsers.add_parser('progress', help='Generate daily progress for subscribed repositories')
    
    # report 命令：生成每日报告
    subparsers.add_parser('report', help='Generate project report from daily progress')
    
    # start-scheduler 命令：启动后台 Scheduler
    subparsers.add_parser('start-scheduler', help='Start the update scheduler in the background')
    
    # stop-scheduler 命令：停止后台 Scheduler
    subparsers.add_parser('stop-scheduler', help='Stop the running update scheduler')

    # add 命令：添加订阅仓库
    parser_add = subparsers.add_parser('add', help='Add a new repository to subscriptions')
    parser_add.add_argument('repository', type=str, help='The repository to subscribe (e.g., username/repo)')

    # remove 命令：移除订阅仓库
    parser_remove = subparsers.add_parser('remove', help='Remove a repository from subscriptions')
    parser_remove.add_argument('repository', type=str, help='The repository to remove (e.g., username/repo)')
    
    # list 命令：列出所有订阅的仓库
    subparsers.add_parser('list', help='List all subscribed repositories')

    # help 命令：显示帮助信息
    subparsers.add_parser('help', help='Show help')

    # 解析参数
    args = parser.parse_args()

    if args.command == 'progress':
        generate_progress()
    elif args.command == 'report':
        generate_report()
    elif args.command == 'start-scheduler':
        start_scheduler()
    elif args.command == 'stop-scheduler':
        stop_scheduler()
    elif args.command == 'add':
        add_subscription(args.repository)
    elif args.command == 'remove':
        remove_subscription(args.repository)
    elif args.command == 'list':
        list_subscriptions()
    elif args.command == 'help' or args.command is None:
        parser.print_help()  # 使用 argparse 自带的帮助功能
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
