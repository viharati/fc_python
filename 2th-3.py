# -*- coding:utf-8 -*-

emails=['a@gmail.com', 'b@naver.com', 'c']
desc = "For developer"
students_count = 10

for val in emails:
	#print(val)

	if '@' not in val:
		print("wrong \t: ",val)
	else:
		print("pass \t: ",val)

print(desc)
desc = desc.replace("developer", "beginner")
print(desc)

if students_count >=5:
	students_count=5
	print("exeed")
