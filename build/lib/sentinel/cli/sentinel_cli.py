import argparse
import threading
from sentinel.services.subscription_service import SubscriptionService
from sentinel.tasks.scheduler import Scheduler
from sentinel.services.update_service import UpdateService

subscription_service = SubscriptionService()
scheduler = None
scheduler_thread = None

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

def get_updates():
    for repo in subscription_service.list_subscriptions():
        update_service = UpdateService(repo)
        updates = update_service.check_updates()
        print(f"Updates for {repo}:")
        print(updates)

def start_scheduler():
    global scheduler, scheduler_thread
    scheduler = Scheduler(subscription_service)
    scheduler_thread = threading.Thread(target=scheduler.start)
    scheduler_thread.daemon = True  # 设置为守护线程，不阻塞主进程
    scheduler_thread.start()
    print("Scheduler started in the background.")

def stop_scheduler():
    global scheduler
    if scheduler:
        scheduler.stop()
    else:
        print("No scheduler is running.")

def print_help():
    help_message = """
GitHub Sentinel 命令行工具

用法:
  gh-sentinel add <repository>          添加新的仓库订阅。
  gh-sentinel remove <repository>       移除已订阅的仓库。
  gh-sentinel list                      列出所有已订阅的仓库。
  gh-sentinel update                    获取所有已订阅仓库的最新更新。
  gh-sentinel start-scheduler           在后台启动更新调度器。
  gh-sentinel stop-scheduler            停止正在运行的更新调度器。
  gh-sentinel help                      显示此帮助信息。

示例:
  gh-sentinel add langchain-ai/langchain  # 添加仓库 langchain-ai/langchain
  gh-sentinel list                        # 列出所有订阅的仓库
  gh-sentinel update                      # 获取订阅仓库的更新
  gh-sentinel start-scheduler             # 启动后台更新调度器
  gh-sentinel stop-scheduler              # 停止后台更新调度器
"""
    print(help_message)

def main():
    parser = argparse.ArgumentParser(prog='gh-sentinel', description='GitHub Sentinel Command Line Tool', add_help=False)
    
    # 定义命令
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # add 命令
    parser_add = subparsers.add_parser('add', help='Add a new repository to subscriptions')
    parser_add.add_argument('repository', type=str, help='The repository to subscribe (e.g., username/repo)')

    # remove 命令
    parser_remove = subparsers.add_parser('remove', help='Remove a repository from subscriptions')
    parser_remove.add_argument('repository', type=str, help='The repository to remove (e.g., username/repo)')
    
    # list 命令
    parser_list = subparsers.add_parser('list', help='List all subscribed repositories')

    # update 命令
    parser_update = subparsers.add_parser('update', help='Get updates for all subscribed repositories')

    # start-scheduler 命令
    parser_scheduler = subparsers.add_parser('start-scheduler', help='Start the update scheduler in the background')

    # stop-scheduler 命令
    parser_stop_scheduler = subparsers.add_parser('stop-scheduler', help='Stop the running update scheduler')

    # help 命令
    parser_help = subparsers.add_parser('help', help='Show help')

    # 解析参数
    args = parser.parse_args()

    if args.command == 'add':
        add_subscription(args.repository)
    elif args.command == 'remove':
        remove_subscription(args.repository)
    elif args.command == 'list':
        list_subscriptions()
    elif args.command == 'update':
        get_updates()
    elif args.command == 'start-scheduler':
        start_scheduler()
    elif args.command == 'stop-scheduler':
        stop_scheduler()
    elif args.command == 'help' or args.command is None:
        print_help()
    else:
        print_help()

if __name__ == "__main__":
    print_help()  # 启动时先打印帮助信息
    main()
