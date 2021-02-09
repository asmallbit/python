names = ["John", "Taylor", "Jack", "Amy", "Tom"]
print(names[-2])
print("Hello, "+names[1])
print("Hello, "+names[-1])

#编辑列表
names[0] = "Delacey"
print(names)

#列表末尾添加元素 使用函数 append()
names.append("Luke")
print(names)

language=[]
language.append("English")
language.append("Japanese")
language.append("French")
print(language)

#在列表中添加元素  使用函数 insert()
language.insert(0,"Chinese")
print(language)

#从列表中删除元素  可使用 del语句,需要知道要删除的元素的索引
del language[0]
print(language)
#方法 pop()可以删除列表末尾的元素,并返回删除的值,在pop()方法的括号中填上索引,即可删除任意元素
popped_language = language.pop()
print(language)
print(popped_language)
print("My language is " + popped_language)
#如果要从列表中删除一个元素，且不再以任何方式使用它，使用del语句；如果要在删除元素后还能继续使用它，就使用方法pop()。
#从列表删除元素还可使用remove()方法
print("The list is "+ str(language))
language.remove("Japanese")
print("Now the list is "+ str(language))

'''
列表中字符串处理
	添加元素 
	insert(int num, String str)		第一个参数为添加后的索引,第二个参数为要添加的字符串
	删除元素
	pop(int num)	参数为要删除的元素在列表中的索引
	remove(String str)		参数为要删除元素的值(String类型)
'''
