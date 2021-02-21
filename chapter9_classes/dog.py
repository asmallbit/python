class Dog():
	#构造函数必须是 __init__, 不能用 _init_
	def __init__(self, name, age):
		#初始化属性name和age
		self.name = name
		self.age = age
		
	def sit(self):
		print(self.name.title()+" is now sitting.")
		
	def roll_over(self):
		print(self.name.title()+" rolled over!")
#创建实例
my_dog = Dog('willie', 6)

print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)

print("\nYour dog's name is "+your_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
your_dog.sit()
