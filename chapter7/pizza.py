prompt="What do you need to add in your pizza"
prompt+="\nInput 'quit' to end the program\n"
message=""
while message != 'quit':
	message=input(prompt)
	if message != "quit":
		print("We will add "+message+" in your pizza.\n")
