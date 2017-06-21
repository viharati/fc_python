# -*- coding:utf-8 -*-

for i in range(10):
	print(i)
	break
	print("!!!")
print("-"*20)

for i in range(10):
	print(i)
	if i<5:
		continue
	print("!!!")