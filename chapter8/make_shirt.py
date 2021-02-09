'''
#练习8-3
def make_shirt(size, string):
	print("The size of this shirt is size "+str(size)+". "+string)

make_shirt(12, string="Hello, guys!")
'''
#练习8-4
def make_shirt(size='large', string='I love python'):
	print("The size of this shirt is "+str(size)+". "+string+"\n")
	
make_shirt()
make_shirt(size='middle')
make_shirt(string='I dont love python!')

#练习8-5
def describe_city(city_name, city_country='england'):
	print(city_name.title()+" is in "+city_country.title())
	
describe_city('london')
describe_city('nanking','china')
describe_city(city_name='atlanta',city_country='america')
