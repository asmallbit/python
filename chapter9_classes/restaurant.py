#Á·Ï°9-1 & 9-4 & 9-6
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print("\nThe restaurant's name is "+self.restaurant_name.title()+", it's a "
			+self.cuisine_type.title()+" restaurant.\nIt served "+str(self.number_served)+" people.")
	
	def open_restaurant(self):
		print(self.restaurant_name.title()+" restaurant is open now.")
	
	def set_number_served(self, person_numbers):
		self.number_served = person_numbers
		
	def increment_number_served(self, person_numbers):
		self.number_served += person_numbers
		
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		
	def icecream_kinds(self, *ice_list):
		self.flavors = []
		for ice in ice_list:
			self.flavors.append(ice)
	
	def describe_icecream(self):
		message = str(self.flavors)
		print("We have these kinds of ice cream:\n\t"+message)

my_restaurant = Restaurant('jim','french')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print()
heb_restaurant = Restaurant('holiday joy','chinese')
heb_restaurant.describe_restaurant()

print()
nj_restaurant = Restaurant('trump','fast food')
nj_restaurant.describe_restaurant()

print()
test_restaurant = Restaurant('test','test')
test_restaurant.number_served = 2000
test_restaurant.describe_restaurant()
test_restaurant.increment_number_served(200)
test_restaurant.describe_restaurant()
test_restaurant.set_number_served(4000)
test_restaurant.describe_restaurant()

print()
#my_icecreamstand = IceCreamStand()
my_icecreamstand = IceCreamStand(restaurant_name='bill',cuisine_type='bill')
my_icecreamstand.icecream_kinds('apple','watermalon','strawbattery')
my_icecreamstand.describe_icecream()
