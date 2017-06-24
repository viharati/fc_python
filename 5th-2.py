from my_email import Email
from my_email_multi import Email as EmailMulti

e = Email()
e.send_mail('yunjy', 'harati@outlook.kr')

emt = EmailMulti(SMTP_SERVER, SMTP_USER, SMTP_PASSWORD, SMTP_PORT)