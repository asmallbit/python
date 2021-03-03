#Á·Ï°10-8 & 10-9
filename1 = 'resource/cats.txt'
filename2 = 'resource/dogs.txt'
try:
	with open(filename1) as f_obj:
		cats_name = f_obj.read()
		cats_name = cats_name.split()
except FileNotFoundError:
	#print("Sorry, the file you need doesnt exist.")
	pass
else:
	for cat_name in cats_name:
		print("This cat's name is "+cat_name.title())
print()

try:
	with open(filename2) as f_obj:
		dogs_name = f_obj.read()
		dogs_name = dogs_name.split()
except FileNotFoundError:
	#print("Sorry, the file you need doesnt exist.")
	pass
else:
	for dog_name in dogs_name:
		print("This dog's name is "+dog_name.title())
