import os
import json

class Config:
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', 'your_token_here')
    NOTIFICATION_EMAIL = 'hmj007007@gmail.com'
    UPDATE_FREQUENCY = 'daily'  # or 'weekly'
    
    @staticmethod
    def get_subscribed_repositories():
        # 从 JSON 文件中加载订阅的仓库
        with open("subscriptions.json", "r") as file:
            config_data = json.load(file)
            return config_data.get('repositories', [])

    @staticmethod
    def init_app(app):
        pass

# 调试：打印当前 Token，确保已正确加载
print(f"Using GitHub Token: {Config.GITHUB_TOKEN}")