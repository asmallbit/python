#Á·Ï°10-5
filename = 'resource\program_reasons.txt'
with open(filename, 'a') as file_object:
	while True:
		reason = input("Why you like programming?\n")
		if not reason:
			break
		file_object.write(reason+"\n")
