#定义元组,元组内元素的值不可改变
dimensions =(200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 100 	TypeError: 'tuple' object does not support item assignment
for dimension in dimensions:
	print(dimension)
#元组元素不能修改,但可以改变存储元组的变量赋值
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
