# import smtplib
#
#
# def send_email(from_addr, to_addr, subject, text, encode='utf-8'):
#     passwd = "mck-H8U-sK9-yqA"
#     server = "smtp.yandex.ru"
#     port = 587
#     charset = f'Content-Type: text/plain; charset={encode}'
#     mime = 'MIME-Version: 1.0'
#     body = "\r\n".join((f"From: {from_addr}", f"To: {to_addr}",
#            f"Subject: {subject}", mime, charset, "", text))
#
#     try:
#         smtp = smtplib.SMTP(server, port)
#         smtp.starttls()
#         smtp.ehlo()
#         smtp.login(from_addr, passwd)
#         smtp.sendmail(from_addr, to_addr, body)
#     except Exception as exc:
#         print('Что - то пошло не так...')
#         raise exc
#     finally:
#         smtp.quit()
#
# if __name__ == "__main__":
#     from_addr = "yudin1ilya@yandex.ru"
#     to_addr = "brawlakkum@gmail.com"
#     subject = "Тестовое письмо от Python."
#     text = "Отправкой почты управляет Python!"
#     send_email(from_addr, to_addr, subject, text)
#!/usr/bin/env python3

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
#
# msg = MIMEMultipart()
# from_email = 'probe.python@gmail.com'
# password = '5MC-LuV-u9z-ciP'
# to_email = 'brawlakkum@gmail.com'
# message = 'Сообщение сделано при помощи python'
#
# msg.attach(MIMEText(message, 'plain'))
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(from_email, password)
# server.sendmail(from_email, to_email, msg.as_string())
# server.quit()
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
#
# msg = MIMEMultipart()
# from_email = 'yudin1ilya@yandex.ru'
# password = 'onpdmxpgyodjznsh' - !!!пароль для приложения, не от почты!!!
# to_email = 'yudin1ilya@yandex.ru'
# message = 'Сообщение сделано при помощи python'
#
# msg.attach(MIMEText(message, 'plain'))
#
# server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
# server.ehlo()
# server.login(from_email, password)
# server.sendmail(from_email, to_email, msg.as_string())
# server.close()
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


for i in range(0, 5):
    sendler('yudin4323@yandex.ru', 'Ну здравствуй!')
