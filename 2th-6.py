import sys
print("python version: ", sys.version[0], type(sys.version[0]))

user_input = ''

while user_input != 'q':
	if(sys.version[0]=='2'):
		user_input = raw_input("Ver2-Input: ")
		print(user_input)
	#elif(sys.version[0]==3):
	else:
		user_input = input("Ver3-Input: ")
		print(user_input)
	#else:
		#user_input = raw_input("Ver2-Input: ")
	
