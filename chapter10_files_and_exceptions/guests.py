#Á·Ï°10-3 & 10-4
filename = 'resource\guest.txt'
file2name = 'resource\guest_book.txt'
with open(filename, 'a') as file_object:
	while True:
		guest_name = input("Please enter your name: ")
		if not guest_name:
			break
		print("Hi, there! "+guest_name.title())
		file_object.write(guest_name.title()+"\n")
		with open(file2name, 'a') as file2_object:
			file2_object.write(guest_name.title()+" loged in.\n")
