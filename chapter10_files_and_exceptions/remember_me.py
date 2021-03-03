'''
import json
#若已存储用户名,则加载它,否则,提示用户输入用户名并存储它
filename = 'resource/username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What's your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, "+username+'!')
else:
	print("Welcome back, "+username+"!")
'''
#another version
import json,os
def get_stored_username():
	filename = 'resource/remember_me.txt'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def get_new_username():
	username = input("What's your name?")
	filename = 'resource/remember_me.txt'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		return username
		
def greet_user():
	username = get_stored_username()
	if username:
		print("Welcome back, "+str(username)+"!")
	else:
		username = get_new_username()
		print("We'll remember your when you come back, "+username+"!")

greet_user()
