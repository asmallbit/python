squares = []
for value in range(1,11,2):
	square = value**2
	#两个**连在一起表示乘方运算,eg x**2 表示x的平方
	squares.append(square)
value = 1
for square in squares:
	print(str(value)+"*"+str(value)+" = "+str(square))
	value += 2
#########################################################
print("*******************************************************")	
#打印乘法口诀表
for i in range(1,10):
	for j in range(1,i+1):
		print(str(i) + "*" + str(j) + "=" + str(i*j), end="\t")
	print()
##############################################################
print("******************************************************")
#列表解析,编写一行代码生成列表
'''
首先指定一个描述性的列表名，如squares；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为value**2，它计算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。在这个示例中，for循环为forvalue in range(1,11)，它将值1～10提供给表达式value**2。请注意，这里的for语句末尾没有冒号.
'''
squares = [value**2 for value in range(2,11,2)]
print(squares)
