cars = ["audi","bwm","subaru","toyota"]

for car in cars:
	if car == "bwm":
		print(car.upper())
	else:
		print(car.title())

car1 = "audi"
car2 = "toyota"
print()
# and
if car1=="audi" and car2=="toyota":
	print("Right!")
else:
	print("Wrong!")
# or
print()
if car1!="audi" or car2=="toyota":
	print("Right!")
else:
	print("Wrong!")
# in
print()
if "audi" in cars:
	print("This list include Audi")
else:
	print("This list doesnt include Audi")

# not in
print()
if "ford" not in cars:
	print("This list doesnt include Ford")
else:
	print("This list include Ford")
