import json
def get_stored_favorite_number(filename):
	with open(filename) as f_obj:
		favorite_number = json.load(f_obj)
		return favorite_number
			
def get_new_favorite_number(filename):
	favorite_number = input("Please inout your favorite number: ")
	with open(filename, 'w') as f_obj:
		json.dump(favorite_number, f_obj)

def favorite_number(filename):
	try:
		favorite_number = get_stored_favorite_number(filename)
	except FileNotFoundError:
		favorite_number = get_new_favorite_number(filename)
		print("I have known your favorite number. I will tell your favorite number when your run me again,.")
	else:
		print("I know your favorite number! It's "+str(favorite_number)+".")
		
filename = 'resource/favorite_numbers.json'
favorite_number(filename)
