def send_mail(from_email, to_email, subj, cont):
	print("from:\t" + from_email)
	print("to:\t" + to_email)
	print("subj:\t" + subj)
	print("cont:")
	print("-"*10)
	print(cont)
	print("-"*10)
	
my_email = "yunjy@snu.ac.kr"

users=[]
users.append({'name':'john', 'email':'john@gmail.com'})
users.append({'name':'joy',  'email':'joy@gmail.com'})

contents = "Thank you"
for users in users:
	title = "Dear. " + str(users['name'])
	send_mail(my_email,users['email'],title,contents)