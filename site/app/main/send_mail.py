import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


MAIL_SERVER_DOMAIN = "smtp.yandex.ru"
MAIL_SERVER_PORT = 587


def send_email(to_email, msg_subject, msg_text):

    try:
        server = smtplib.SMTP(MAIL_SERVER_DOMAIN, MAIL_SERVER_PORT)
    except:
        raise Exception("Bad connection or Settings of server are incorrect")

    server.starttls()
    try:
        server.login(FROM_MAIL, PASSWORD)
    except:
        raise Exception("Bad login or password")

    msg = MIMEMultipart()
    msg["subject"] = msg_subject
    msg.attach(MIMEText(msg_text))

    server.sendmail(from_addr = FROM_MAIL, to_addrs = to_email, msg = msg.as_string())
    server.quit()

    print("Email successfully sent")
