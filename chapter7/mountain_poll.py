responses={}

#设置一个标志,指出调查是否继续
polling_active = True
while polling_active:
	#提示输入被调查者的名字和回答
	name = input("\nWhat's your name?")
	response = input("Which mountain would you like to climb someday?")
	
	#将答案存储在字典中
	responses[name] = response
	
	#看看是否还有人要参与调查
	repeat = input("Would you like to let another person respond?(y/n)")
	#设置一个标志,指出循环是否继续
	loop = False
	
	if repeat.lower() == 'no' or repeat.lower() == 'n':
		polling_active = False
	elif repeat.lower() == 'yes' or repeat.lower() == 'y':
		print("Thank you, please let other guys answer this quertion.")
	#解决用户输入错误的问题
	else:
		loop = True
		while loop:
			end_loop = input("Sorry, Please enter 'yes(y)' or 'no(n)'\n")
			if end_loop.lower() == ('y' or 'yes'):
				print("Thank you, please let other guys answer this question.")
				loop = False
			if end_loop.lower() == ('n' or 'no'):
				polling_active = False
				loop = False
#调查结束,显示结果
print("\n--- Poll Results ---")
for name,response in responses.items():
	print(name.title()+" would loke to climb "+response+".")
