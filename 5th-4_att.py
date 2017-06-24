#coding: utf-8
from my_email import Email

e = Email()
e.send_mail('윤준연', 'harati@outlook.kr')
e.send_mail('윤준연', 'harati@outlook.kr', 'emails.xlsx')
e.send_mail('윤준연', 'harati@outlook.kr', 'd:\emails.xlsx')