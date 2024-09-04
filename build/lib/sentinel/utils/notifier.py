import smtplib
from email.mime.text import MIMEText
from sentinel.config import Config

class NotificationService:
    def __init__(self):
        self.recipient = Config.NOTIFICATION_EMAIL

    def send_email(self, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = 'hmj007007@gmail.com'
        msg['To'] = self.recipient

        with smtplib.SMTP('smtp.gmail.com') as server:
            server.login('hmj007007', 'A5a4B1c8D8eZ%')
            server.sendmail('hmj007007@gmail.com', [self.recipient], msg.as_string())
