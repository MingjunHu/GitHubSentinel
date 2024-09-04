import os

class Config:
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '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')
    REPOSITORIES = ['langchain-ai/langchain']
    NOTIFICATION_EMAIL = 'hmj007007@gmail.com'
    UPDATE_FREQUENCY = 'daily'  # or 'weekly'

    @staticmethod
    def init_app(app):
        pass
