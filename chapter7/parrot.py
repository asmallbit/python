prompt="Tell me something, I will repeat it back it to you: "
prompt+="\nEntter 'quit' or 'exit' to end the program.\n"

#使用标志
active=True
while active:
	message=input(prompt)
	
	if message=='quit' or 'exit':
		active=False
	else:
		print(message+"\n")
