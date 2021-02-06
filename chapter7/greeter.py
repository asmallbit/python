name=input("Please input your name: ")
print("Hello, "+name.title()+"!")

#提示较长时,可以采取如下方式分开
prompt="If you tell me who you are, we can personalize the messages you see."
prompt+="\nWhat's your first name?"
prompt+="\nEnter 'quit' to end the program.\n"
name=""
#控制程序何时退出,输入quit时退出
while name!="quit":
	name=input(prompt)
	if name!='quit':
		print("Hello, "+name.title())
