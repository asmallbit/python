message="What's your age?\n"
message+="Enter 'quit' to end the program.\n"
age=""
while True:
	age=input(message)
	if(age!='quit'):
		if int(age)<3:
			ticket_price='free'
			print("Your ticket is "+ticket_price)
		elif int(age)<12:
			ticket_price=10
			print("Your ticket price is $"+str(ticket_price))
		else:
			ticket_price=15
			print("Your ticket price is $"+str(ticket_price))
	else:
		break
