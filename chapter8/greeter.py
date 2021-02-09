def greet_user(username):
	print("Helllo, "+username.title()+"!")
	
greet_user('jwhan')

#位置实参,传递给函数时,需要考虑参数的先后顺序
#关键字实参,需递给函数时,无需考虑参数的先后顺序,但要准去指定函数定义的形参名

print()
print("**********************************************************")
print()

#关键字实参

def pet(animal_type, pet_name):
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
pet(animal_type='hamster',pet_name='harry')

print()

#默认值 可设定形参的默认值,在调用函数时,就可不提供已经设定默认值的参数
def pet_dog(pet_name, animal_type='dog'):	#两个形参的位置不能互换
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

#等效的函数调用 由于可混合使用位置实参\关键字实参和默认值,函数的调用方式通常不唯一,如下所示

#一条名为Willie的小狗	
pet_dog('willie')

#一只名为Harry的仓鼠
pet_dog('harry','hamster')
pet_dog(pet_name='harry',animal_type='hamster')
pet_dog(animal_type='hamster',pet_name='harry')

#传递列表
def greet_users(names):
	#向列表中每位用户都发出简单问候
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
		
user_names = ['hannah', 'ty', 'margot']
greet_users(user_names)
print()

#列表作为参数测试
def change_list0(my_list):
	my_list[0] = 7
	
def change_list1(my_list):
	my_list = []
	
def change_list2(my_list):
	#用[]替换my_list中的每一个元素
	#详见:https://stackoverflow.com/questions/11297774/what-is-the-difference-between-a-b-and-a-b
	my_list[:] = []

l0 = [1,2,3]
change_list0(l0)
print("After function change_list0: "+str(l0))	#[7,2,3]
l1 = [1,2,3]
change_list1(l1)
print("After function change_list1: "+str(l1))	#[1,2,3]
l2 = [1,2,3]
change_list2(l2)
print("After function change_list2: "+str(l2))	#[]
print()

#两个变量指向同一个对象
a = [1,2,3,4]
b = a
c = a[:]

print(str(a)+"\n"+str(b)+"\n"+str(c))
print("a: "+str(id(a)))	#视为参照值
print("b: "+str(id(b)))	#与参照值相同
print("c: "+str(id(c)))	#与参照值不同
print("a[:]:"+str(id(a[:])))

'''
传递一个对象作为参数，在函数内给参数重新赋值，就是一个新的对象了，与原对象无关，但是如果对原对象做修改，原对象就会被修改,从而原对象发生改变,此处感谢@Mr.R的帮助
'''
#关于python的参数问题
#使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。	
#https://stackoverflow.com/questions/24719368/syntaxerror-non-default-argument-follows-default-argument/39942121
#https://stackoverflow.com/questions/16932825/why-cant-non-default-arguments-follow-default-arguments
#In python that is how the structure is when you define a function 示例
#def myfunction(position_parameter, *parameter, **keywords)
