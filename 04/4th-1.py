# -*- coding:utf-8 -*-

datafile = open('text2.txt', 'r')
data = datafile.read()

print(data+'\n\n')
string=data.decode('utf-8').encode('euc-kr')
print(string)

