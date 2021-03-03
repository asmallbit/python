def adding(first_number, second_number):
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("Wrong input, please check your input.")
	else:
		return answer
print("This is a adding calculater")
while True:
	first_number = input("Please enter the first number: ")
	second_number = input("Please enter the second number: ")
	print(adding(first_number,second_number))
