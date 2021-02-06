#练习7-8
sandwiches_orders = ['pastrami','pastrami','reuben','club','pastrami','smoked meat','shawarma','doner']
finished_sandwiches=[]
loop = True
#删除列表中所有的'pastrami'元素
while 'pastrami' in sandwiches_orders:
	sandwiches_orders.remove('pastrami')
print("All pastrami has saled out!\n")
while loop:
	if not len(sandwiches_orders):
		loop = False
		print("\nAll sandwiches have been finished:")
		for sandwiche in finished_sandwiches:
			print("\t"+sandwiche)
	else:
		sandwiche = sandwiches_orders.pop()
		print("I made your sandwiche "+sandwiche+" sandwiche.")
		finished_sandwiches.append(sandwiche)
