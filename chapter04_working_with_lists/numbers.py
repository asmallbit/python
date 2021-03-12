for value in range(1,6):
	print(value)
	
#使用range()创建数字列表
numbers = list(range(1,6))
print(numbers)

#打印1~10以内的偶数,步长为2
even_numbers = list(range(2,11,2))
print(even_numbers)

#打印1~20
print("**********************************")
for value in range(1,21):
	print(value)

#创建列表并打印
print("**********************************")
values =list(range(1,1000001))
print("min = "+str(min(values))+", max = "+str(max(values)))
print("1+2+3+...+1000000 = "+str(sum(values)))

#创建奇数列表并打印
print("**********************************")
values = list(range(1,21,2))
for value in values:
	print(value)

#3~30能被3整除的数字
print("***********************************")
values = list(range(3,31,3))
print("?/3 = 0?")
for value in values:
	print(value)
	
#1~10的立方
print("***********************************")
values = list(range(1,11))
for value in values:
	print(str(value)+"*"+str(value)+"*"+str(value)+" = "+str(value**3))

#列表解析包含前10个整数的平方
values = list(value**3 for value in range(1,11))
print(values)
