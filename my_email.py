# -*- coding: utf-8 -*- 
class Email():
	from_email = ''
	to_email	= ''
	subject		= ''
	contents	= ''

	def send_mail(self):
		string1 = "From: " + self.from_email 
		string2 = "To  : " + self.to_email + '\n'
		print(string1)
		print(string2)

def get():
	pass

def set():
	pass