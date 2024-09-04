import smtplib
from email.mime.text import MIMEText
from sentinel.config import Config

class NotificationService:
    def __init__(self):
        self.recipient = Config.NOTIFICATION_EMAIL

    def send_email(self, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = 'sentinel@example.com'
        msg['To'] = self.recipient

        with smtplib.SMTP('smtp.example.com') as server:
            server.login('username', 'password')
            server.sendmail('sentinel@example.com', [self.recipient], msg.as_string())
