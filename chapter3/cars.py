cars = ["bwm", "audi", "toyota","subaru","byd"]
cars.sort()
#sort()	将列表元素永久性排序,不可逆		sort(reverse=True) 逆序,同样不可逆
print("Here is the original list:\n"+str(cars))
cars.sort(reverse=True)
print("Here is the sorted list:\n"+str(cars))
#sorted() 可进行临时排序,并不会改变原来的排列顺序, 同样,也可向sorted()方法传递参数reserve=True
print("Here is the original list again:\n" + str(sorted(cars)))
###################################################################
print("\n************************************************************\n")
#reverse()方法可以反转列表元素的排列顺序
cars = ["bwm", "audi", "toyota","subaru","byd"]
print(cars)
cars.reverse()
print(cars)
#len()方法可用于获取列表长度
length = len(cars)
print("This list length is "+str(length))

'''
列表元素排序
	sort()	按字典顺序排序,不可逆		sort(reverse=True)	按与字典顺序相反的顺序排序
	sorted( )	参数为列表名称,并不会改变列表本身的值
	reverse()	将列表元素顺序反转
列表长度
	len()	用于获取列表元素个数
'''
