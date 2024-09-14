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
    exec_time="08:00"

    def __init__(self):
        self.load_config()
    
    @staticmethod
    def get_subscribed_repositories():
        # 从 JSON 文件中加载订阅的仓库
        with open("subscriptions.json", "r") as file:
            config_data = json.load(file)
            return config_data.get('repositories', [])

    @staticmethod
    def init_app(app):
        pass
    
    def load_config(self):
        # 尝试从环境变量获取配置或使用 config.json 文件中的配置作为回退
        with open('config.json', 'r') as f:
            config = json.load(f)
            
            # 使用环境变量或配置文件的 GitHub Token
            self.github_token = os.getenv('GITHUB_TOKEN', config.get('github_token'))

            # 初始化电子邮件设置
            self.email = config.get('email', {})
            # 使用环境变量或配置文件中的电子邮件密码
            self.email['password'] = os.getenv('EMAIL_PASSWORD', self.email.get('password', ''))

            self.subscriptions_file = config.get('subscriptions_file')
            # 默认每天执行
            self.freq_days = config.get('github_progress_frequency_days', 1)
            # 默认早上8点更新 (操作系统默认时区是 UTC +0，08点刚好对应北京时间凌晨12点)
            self.exec_time = config.get('github_progress_execution_time', "08:00") 

            # 加载 LLM 相关配置
            llm_config = config.get('llm', {})
            self.llm_model_type = llm_config.get('model_type', 'openai')
            self.openai_model_name = llm_config.get('openai_model_name', 'gpt-4o-mini')
            self.ollama_model_name = llm_config.get('ollama_model_name', 'llama3')
            self.ollama_api_url = llm_config.get('ollama_api_url', 'http://localhost:11434/api/chat')

# 调试：打印当前 Token，确保已正确加载
#print(f"Using GitHub Token: {Config.GITHUB_TOKEN}")