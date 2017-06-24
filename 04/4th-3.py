import sys
if(sys.version[0]=='2'):
	user_input = raw_input("Input: ")
else:
	user_input = input("Input: ")
datafile = open('output.txt','a')

datafile.write(user_input)
