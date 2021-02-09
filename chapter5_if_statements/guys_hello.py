guys=["admin","josh","mosh","taylor","amy"]
login_guys=["mosh","amy","admin","taylor"]
if login_guys:
	for login_guy in login_guys:
		if login_guy=="admin":
			print("Hello "+login_guy+", would you like to see a status report?")
		elif login_guy in guys:
			print("Hello "+login_guy.title()+", thank you for logging in again")
else:
	print("We need to find some users!")

print("******************************************************")
current_users=["jack","rose","luke","husson","joHNson"]
current_users_lower=[]
for current_user in current_users:
	current_users_lower.append(current_user.lower())
new_users=["jill","lucy","jack","Johnson","alice"]
for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print("Sorry, this username '"+ new_user+"' has been used. Change another username.")
	else:
		print("Good! your username is "+new_user+" now!")
