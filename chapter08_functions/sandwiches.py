#练习8-12
def make_sandwiches(*toppings):
	print("\nWe are making sandwiches. The toppings are here: ")
	for topping in toppings:
		print("- "+topping)
		
make_sandwiches('mashroom','pipcone')
make_sandwiches('test0','test1','test2','test3')
make_sandwiches('mushrooms','green peppers','extra cheese')
print()
#练习8-14
def make_car(maker, model, **other_info):
	#创建一个名为car_profile的空字典
	car_profile={}
	car_profile['maker']=maker
	car_profile['model']=model
	for key, value in other_info.items():
		car_profile[key]=value
	return car_profile
		
car = make_car('subaru','outback',color='blue',tow_package=True)
print("The car information:\n"+str(car))
