#传递任意数量的形参
#形参名*toppings中的星号使python创建一个名为toppings的空元组,并将收到的所有值都封装到这个元组中
def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)
	
#make_pizza('pepperoni')
#make_pizza('mushrooms','green peppers','extra cheese')

#结合使用位置实参和任意参数实参
#注意:要让函数接受不同类型的实参,必须在函数定义中接纳任意数量实参的形参放在最后
def make_pizza2(size, *toppings):
	print("\nMaking a "+str(size)+
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)
		
#make_pizza2(16,'pepperoni')
#make_pizza2(12,'mushroom','green peppers','extra cheese')

#使用任意数量的关键字实参
