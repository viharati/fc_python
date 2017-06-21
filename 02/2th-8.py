person = {'name':'a', 
			'age':30, 
			'phone':'01000000000'}

print(person.keys())
print(person.values())
print(person.items())

for key in person.keys():
	print('key is ', key)
	print('val is ', person[key])

print("-"*10)

for value in person.values():
	print('val is ',value)

print("-"*10)

for (key, val) in person.items():
	print('key is ', key)
	print('val is ', val)
