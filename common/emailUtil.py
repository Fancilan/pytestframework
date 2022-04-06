import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["mail"]

# 第三方 SMTP 服务
mail_host = data['MAIL_HOST']  # 设置服务器
mail_user = data['MAIL_ACCOUNT']  # 用户名
mail_pass = data['MAIL_PASSWORD']  # 口令

sender = data['MAIL_ACCOUNT']  # 发送者的邮箱
receivers = [data['MAIL_ACCOUNT']]  # 接收邮件，其他人的邮箱

mail_msg = """
<p>HTML邮件测试</p>
"""

# 设置为html邮箱

message = MIMEMultipart('mixed')

# 标准邮件需要三个头部信息： From, To, 和 Subject
message["From"] = Header("测试人员", "utf-8")  # 发送人
message["To"] = Header("自己", "utf-8")  # 接收人

subject = 'HTML邮件测试'
message['Subject'] = Header(subject, 'utf-8')  # 邮件主题

# att1 = MIMEText(open("E:\\work\\自动化测试框架\\pytestDemo\\testcases\\reports\\index.html", "rb").read(), "base64", "utf-8")
# # 文件地址
# att1["Content-Type"] = "application/octet-stream"
# att1["Content-Disposition"] = 'attachment; filename="index.html"'
# # 定义附件名称
# message.attach(att1)

if __name__ == '__main__':
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.connect(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        logger.info("sucess:邮件发送成功！")
        smtpObj.quit()
    except smtplib.SMTPException:
        logger.error("error:邮件发送失败！")