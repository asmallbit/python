pizzas = ["marinara","margherita","romana","napoletana"]
for pizza in pizzas:
	print(pizza.title())
	print("I like "+pizza+" pizza.")
print("I really love "+pizza+" pizza.")
edited_pizzas = pizzas[:]
pizzas.append("siciliana")

#ÁªÏµ4-11
print("*****************************************")
print("My favorite pizza is:")
for pizza in pizzas:
	print(str(pizza)+" pizza")
print("*****************************************")
print("My friend's favorite pizza is: "+str(edited_pizzas))
for edited_pizza in edited_pizzas:
	print(str(edited_pizza)+" pizza")
