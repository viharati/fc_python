# coding:utf-8
import sys
print ("python version: " + str(sys.version[0]))
if(sys.version[0]=='2'):
	from email.MIMEMultipart import MIMEMultipart
	from email.MIMEText import MIMEText
else:
	#python3
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_USER = 'pasyati0@gmail.com'
SMPT_PASSWORD ='rufwjd09'


SMPT_PORT=465

def send_mail(name, add):
	import smtplib

	#텍스트 메일을 보낼 때 사용하는 타입	
	msg = MIMEMultipart('alternative')
	#서버에서 스팸처리를 하는데 이걸 피하기 위함
	msg['From'] = SMTP_USER
	msg['To']	= addr
	msg['Subject'] = '자동화메일입니다.'.decode('utf-8')

	contents = name.decode('utf-8') + '님. 안녕하세요.'.decode('utf-8')

	#추가하는 내용이 txt이므로  MIMEText로 만들어서 넣음.
	mime_text = MIMEText(contents, _charset='utf-8')
	msg.attach(mime_text)
	#msg.attach(MIMEText(contents, _charset='utf-8'))

	smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
	smtp.login(SMTP_USER, SMTP_PASSWORD)
	smtp.sendmail(SMTP_USER, addr, msg.as_string())
	smtp.close()

