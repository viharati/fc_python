# coding:utf-8
datafile=open('text2.txt','r')

while True:
	line = datafile.readline()
	if not line:
		break

	print(line.strip())
	#print(line.decode('utf-8'))