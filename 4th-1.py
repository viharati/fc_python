# -*- coding:utf-8 -*-

datafile = open('text.txt', 'r')
data = datafile.read()

print(data)
string=data.decode('utf-8').encode('euc-kr')
print(string)

