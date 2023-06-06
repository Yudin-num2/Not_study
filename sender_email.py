import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendler(to_email, message):
    server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
    msg = MIMEMultipart()
    password = "onpdmxpgyodjznsh"
    msg['From'] = "yudin1ilya@yandex.ru"
    msg['To'] = to_email
    msg['Subject'] = "Subscription"
    msg.attach(MIMEText(message, 'plain'))
    server.ehlo()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.close()


for i in range(0, 10):
    sendler('n.korol14@mail.ru', 'Ну здравствуй, Анастас-Ананас!')
