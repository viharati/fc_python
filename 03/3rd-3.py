def myprint(string):
	if 'bad' in string:
		print('Rejected')
		return
	else:
		print(string)

	print("-"*10)

user_input=''
while user_input != 'quit':
	#user_input = raw_input("input: ")
	user_input = input("input: ")
	myprint(user_input)
