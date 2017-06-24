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



class Email:
	def __init__(self, SMTP_SERVER='smtp.gmail.com', SMTP_USER='pasyati0@gmail.com', SMTP_PASSWORD = 'rufwjd09', SMTP_PORT=465):
		self.SMTP_SERVER 	= SMTP_SERVER
		self.SMTP_USER = SMTP_USER
		self.SMTP_PASSWORD = SMTP_PASSWORD
		self.SMTP_PORT = SMTP_PORT 

	subj_layout = "님에게 메일이 도작했습니다. "
	cont_layout = """님 안녕하세요."
자동화로 발송되는 메일입니다 .
"""#.decode('utf-8')

	
	
	def send_mail(self, name, addr):
		import smtplib
		postfix= "python version: " + str(sys.version[0]) + " 에서 보냄"

		#텍스트 메일을 보낼 때 사용하는 타입	
		msg = MIMEMultipart('alternative')
		#서버에서 스팸처리를 하는데 이걸 피하기 위함
		msg['From'] = self.SMTP_USER
		msg['To']	= addr
		#msg['Subject'] = '자동화메일입니다.'
		#msg['Subject'] = '자동화메일입니다.'.decode('utf-8')
		msg['Subject'] = name + self.subj_layout
		
		#contents = name.decode('utf-8') + '님. 안녕하세요.'.decode('utf-8')
		contents = name + '님. 안녕하세요.\n' + postfix
		contents = name + self.cont_layout + postfix

		#추가하는 내용이 txt이므로  MIMEText로 만들어서 넣음.
		mime_text = MIMEText(contents, _charset='utf-8')
		msg.attach(mime_text)
		#msg.attach(MIMEText(contents, _charset='utf-8'))

		smtp = smtplib.SMTP_SSL(self.SMTP_SERVER, self.SMTP_PORT)
		#smtp= smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		#smtp.ehlo()
		#smtp.esmtp_features['auth'] = "LOGIN PLAIN"

		smtp.login(self.SMTP_USER, self.SMTP_PASSWORD)
		smtp.sendmail(self.SMTP_USER, addr, msg.as_string())
		smtp.close()