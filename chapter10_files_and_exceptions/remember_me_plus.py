'''
#version1
import json
def read_stored_user(filename):
	with open(filename) as f_obj:
		username = json.load(f_obj)
		return username

def add_new_user(filename):
	username = input("Please enter you name: ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username
		
def greet_user(filename):
	try:
		username = read_stored_user(filename)
	except FileNotFoundError:
		username = add_new_user(filename)
		print("I have remember your name. I will tell your name when you run me next time.")
	else:
		while True:
			option = input("Are you "+str(username).title()+"? Please enter Y or N.\n")
			if option.upper() == 'Y':
				print("Hi, there! "+str(username).title()+".")
				break
			elif option.upper() == 'N':
				username = add_new_user(filename)
				print("I have remember your name. I will tell your name when you run me next time.")
				break
			else:
				print("Please enter Y or N.\n")
filename = 'resource/remember_me_plus.txt'
greet_user(filename)
'''

#version2
import json
def read_store_user(filename):
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username
		
def add_new_user(filename):
	username = input("Please enter your name. ")
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username
	
def greet_user(filename):
	username = read_store_user(filename)
	if username:
		print("Are you "+username.title()+"?")
		while True:
			option = input("Please enter Y or N.\n")
			if option.lower() == 'y':
				print("Hi, there! "+username.title()+"! Welcome back.")
				break
			elif option.lower() == 'n':
				username = add_new_user(filename)
				print("Hi, "+username.title()+". I remember your name. I will show your name when you run me again.")
				break
			else:
				print("Sorry, wrong input. Please enter Y or N")
	else:
		add_new_user(filename)
		print("Hi, "+username.title()+". I remember your name. I will show your name when you run me again.")
		
filename = 'resource/remember_me_plus.json'
greet_user(filename)
	
