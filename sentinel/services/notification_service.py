import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sentinel.config import Config
import markdown2
from sentinel.logger import LOG

class NotificationService:
    def __init__(self):
        self.recipient = Config.NOTIFICATION_EMAIL
        self.email_username=Config.EMAIL_USERNAME
        self.email_password=Config.EMAIL_PASSWORD

    def send_email(self, subject, message):
        LOG.info("准备发送邮件")
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.email_username
        msg['To'] = self.recipient
        # 将Markdown内容转换为HTML
        html_report = markdown2.markdown(message)

        msg.attach(MIMEText(html_report, 'html'))

        try:
            with smtplib.SMTP_SSL('smtp.qq.com',465) as server:
                server.login(msg['From'], 'wsfrunybtnsocadi')
                server.sendmail(msg['From'], msg['To'], msg.as_string())
        except Exception as e:
            LOG.error(f"发送邮件失败：{str(e)}")
