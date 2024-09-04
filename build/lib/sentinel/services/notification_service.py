import smtplib
from email.mime.text import MIMEText
from sentinel.config import Config

class NotificationService:
    def __init__(self):
        self.recipient = Config.NOTIFICATION_EMAIL

    def send_email(self, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = '116101982@qq.com'
        msg['To'] = self.recipient

        with smtplib.SMTP_SSL('smtp.qq.com',465) as server:
            server.login('116101982@qq.com', 'wsfrunybtnsocadi')
            server.sendmail('116101982@qq.com', [self.recipient], msg.as_string())
