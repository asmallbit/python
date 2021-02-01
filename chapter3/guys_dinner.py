guys_name = ["John", "Husson", "Rose", "Amy", "Luke"]
num = 0
for num in range(0,5):
	print("Hey, "+guys_name[num]+"!")
	num += 1
print("Let's have the dinner!")

popped_guy = guys_name.pop(2)
print("Sorry, " + popped_guy +" cant come")
#remove()方法	guy_names.remove(2)		del语句也可使用	del guy_names[2]
another_guy = "Taylor"
guys_name.append(another_guy)
print("Another guy "+another_guy+" joined us!")
guys_name.insert(2,"Lucy")
guys_name.insert(0,"Alex")
print("Now the list is "+str(guys_name))

print("*************************************************************************")
num2 = 0
for num2 in range(0,7):
	print("Welcome, "+guys_name[num2])
	num2 += 1
print("All done!")
print("*************************************************************************")

print("Sorry, guys! I dont have enough food! We need less people")

num3=6
while num3>1:
	popped_guy = guys_name.pop(2)
	print("Sorry, "+ popped_guy +" I dont have enough food to treat you.")
	num3 = num3 - 1
print("Please come to my home to have dinner "+ guys_name[0] +" and "+ guys_name[1])
length = len(guys_name)
print("Now we have "+str(length)+" guys to enjoy dinner")
#将剩余的两个也删除
print("deit the list again, delete all guys!")
del guys_name[0]
del guys_name[0]
print("Now the list is "+str(guys_name))
