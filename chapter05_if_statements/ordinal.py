numbers=list(range(1,10))
for number in numbers:
	if number==1:
		print(str(number)+"st")
	elif number==2:
		print(str(number)+"nd")
	elif number==3:
		print(str(number)+"rd")
	elif number==4:
		print(str(number)+"th")
	elif number==5:
		print(str(number)+"th")
	elif number==6:
		print(str(number)+"th")
	elif number==7:
		print(str(number)+"th")
	elif number==8:
		print(str(number)+"th")
	else:
		print(str(number)+"th")
'''
在条件测试的格式设置方面，PEP 8提供的唯一
建议是，在诸如==、>=和<=等比较运算符两边各添加一个空格，例如，if age < 4:要比if age<4:好。
'''
