class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		#给属性指定默认值
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		long_name = str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
		
	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")
		
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cant roll back an odometer!")
			
	def increment_odometer(self, miles):
		self.odometer_reading += miles

#继承	定义子类时,父类需包含在当前文件中,且在子类前面	
class ElectricCar(Car):
	
	def __init__(self, make, model, year):
		super().__init__(make, model, year)		#此处参数中没有self
		self.battery = Battery()
		
	#def describe_battery(self):
		#print("This car has a " + str(self.battery_size) + "-kWh battery.")

class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
		
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def get_range(self):
		if self.battery_size == 70:
			range = 240
			
		elif self.battery_size == 85:
			range = 270
			
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
		
	def update_battery(self):
		self.battery_size = 85

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(3000)
my_new_car.update_odometer(2000)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print("\n"+my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#从某个py文件导入某个类   from file_name import class_name
