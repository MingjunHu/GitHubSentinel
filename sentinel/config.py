# sentinel/config.py
import os
import json

class Config:
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', 'your_token_here')

    # 新增配置
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key')
    EMAIL_USERNAME=os.getenv('EMAIL_USERNAME','hmj007007@gmail.com')
    EMAIL_PASSWORD=os.getenv('EMAIL_PASSWORD','hmj007007@gmail.com')

    NOTIFICATION_EMAIL = os.getenv('NOTIFICATION_EMAIL','hmj007007@gmail.com')
    UPDATE_FREQUENCY = 'daily'  # or 'weekly'

    freq_days = 1
    
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
#print(f"Using GitHub Token: {Config.GITHUB_TOKEN}")