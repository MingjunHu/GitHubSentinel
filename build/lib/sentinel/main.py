from sentinel.services.subscription_service import SubscriptionService
from sentinel.tasks.scheduler import Scheduler

def main():
    # 初始化订阅服务
    subscription_service = SubscriptionService()
    
    # 启动定时任务调度器
    scheduler = Scheduler(subscription_service)
    scheduler.start()

if __name__ == "__main__":
    main()
