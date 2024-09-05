# sentinel/cli/parser.py

import argparse
from sentinel.daily_progress import generate_daily_progress
from sentinel.report_generator import ReportGenerator
from sentinel.tasks.scheduler import Scheduler
from sentinel.services.subscription_service import SubscriptionService
import threading

class CLI:
    def __init__(self):
        self.subscription_service = SubscriptionService()
        self.report_generator = ReportGenerator()
        self.scheduler = None
        self.scheduler_thread = None

    def start_scheduler(self):
        self.scheduler = Scheduler(self.subscription_service)
        self.scheduler_thread = threading.Thread(target=self.scheduler.start)
        self.scheduler_thread.daemon = True  # 守护线程
        self.scheduler_thread.start()
        print("Scheduler started in the background.")

    def stop_scheduler(self):
        if self.scheduler:
            self.scheduler.stop()
            print("Scheduler stopped.")
        else:
            print("No scheduler is running.")

    def generate_progress(self):
        print("Generating daily progress...")
        generate_daily_progress()

    def generate_report(self):
        print("Generating report from daily progress...")
        self.report_generator.generate_formal_reports()

    def print_help(self):
        help_message = """
GitHub Sentinel v0.2 命令行工具

用法:
  main.py progress            生成订阅项目的每日进展 Markdown 文件。
  main.py report              基于每日进展生成项目报告。
  main.py start-scheduler     在后台启动更新调度器。
  main.py stop-scheduler      停止后台更新调度器。
  main.py help                显示此帮助信息。

示例:
  python main.py progress        # 生成每日进展 Markdown 文件
  python main.py report          # 生成正式报告
  python main.py start-scheduler # 启动后台更新调度器
  python main.py stop-scheduler  # 停止后台更新调度器
"""
        print(help_message)

    def parse_arguments(self):
        parser = argparse.ArgumentParser(prog='GitHub Sentinel', description='GitHub Sentinel Command Line Tool', add_help=False)
        
        # 定义子命令
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # progress 命令：生成每日进展 Markdown 文件
        subparsers.add_parser('progress', help='Generate daily progress for subscribed repositories')
        
        # report 命令：生成每日报告
        subparsers.add_parser('report', help='Generate project report from daily progress')
        
        # start-scheduler 命令：启动后台 Scheduler
        subparsers.add_parser('start-scheduler', help='Start the update scheduler in the background')
        
        # stop-scheduler 命令：停止后台 Scheduler
        subparsers.add_parser('stop-scheduler', help='Stop the running update scheduler')
        
        # help 命令：显示帮助信息
        subparsers.add_parser('help', help='Show help')
        
        args = parser.parse_args()
        return args

    def execute_command(self, args):
        if args.command == 'progress':
            self.generate_progress()
        elif args.command == 'report':
            self.generate_report()
        elif args.command == 'start-scheduler':
            self.start_scheduler()
        elif args.command == 'stop-scheduler':
            self.stop_scheduler()
        else:
            self.print_help()

def main():
    cli = CLI()
    args = cli.parse_arguments()
    if not args.command:
        cli.print_help()
    else:
        cli.execute_command(args)

if __name__ == "__main__":
    main()
