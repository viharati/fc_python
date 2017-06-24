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

SMTP_SERVER     = 'smtp.gmail.com'
SMTP_USER       = 'pasyati0@gmail.com'
SMTP_PASSWORD   = 'rufwjd09'
SMTP_PORT=465 # SSL:465, normal:587

class Email():
    subj_layout = "님에게 메일이 도작했습니다. "
    cont_layout = """님 안녕하세요."
자동화로 발송되는 메일입니다 .
"""#.decode('utf-8')

    
    
    def send_mail(self, name, addr, attatchment = None):
        import smtplib
        postfix= "python version: " + str(sys.version[0]) + " 에서 보냄"

        #텍스트 메일을 보낼 때 사용하는 타입   
        msg = MIMEMultipart('alternative')
        #서버에서 스팸처리를 하는데 이걸 피하기 위함
        if attatchment:
            msg = MIMEMultipart('mixed')


        msg['From'] = SMTP_USER
        msg['To']   = addr
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

        if attatchment:
            from email.MIMEBase import MIMEBase
            from email import Encoders
            #python3
            from email.mime.base import MIMEBase
            from email import encoders
            #class 변수 file_data
            file_data = MIMEBase('application', 'octet-stream')#일반 모든 파일을 의미)
            
            #내용은 open 후 read()를 통해 전체 내용을 추가
            #rb 는 binary 컴퓨터가 읽을 수 있는 형태 
            file_data.set_payload(open(attatchment,'rb').read())

            #전송가능한 형태 : serialize 를 해야 조합해서 원본을 만들 수 있다.
            Encoders.encode_base64(file_data)
            #python3
            #encoders.endoce_base64(file_data)

            #헤더에 파일'명'을 추가 이거 없으면 Noname
            #메타데이터, 데이터를 위한 데이터 
            import os
            filename = os.path.basename(attatchment)
            file_data.add_header('Content-Disposition', 'attachment; filename='+filename + '"')
            

            msg.attach(file_data)



        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        #smtp= smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #smtp.ehlo()
        #smtp.esmtp_features['auth'] = "LOGIN PLAIN"

        smtp.login(SMTP_USER, SMTP_PASSWORD)
        smtp.sendmail(SMTP_USER, addr, msg.as_string())
        smtp.close()