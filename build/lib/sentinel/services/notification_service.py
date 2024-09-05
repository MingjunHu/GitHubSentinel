import smtplib
from email.mime.text import MIMEText
from sentinel.config import Config

class NotificationService:
    def __init__(self):
        self.recipient = Config.NOTIFICATION_EMAIL
        self.email_username=Config.EMAIL_USERNAME
        self.email_password=Config.EMAIL_PASSWORD

    def send_email(self, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.email_username
        msg['To'] = self.recipient

        with smtplib.SMTP_SSL('smtp.qq.com',465) as server:
            server.login(self.email_username, 'wsfrunybtnsocadi')
            server.sendmail(self.email_username, [self.recipient], msg.as_string())
