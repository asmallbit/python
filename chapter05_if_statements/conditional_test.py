str1 = "jwhan"
str2 = "Johnson"
str3 = "john"
str4 = "JWHan"
#values的值将以int形式存储
values = [value**2 for value in range(1,10)]
if str1.upper()==str4.upper():
	print(str1+" = "+str4)
else:
	print(str1+" != "+str4)
if str2.lower()==str3.lower():
	print(str2+" = "+str3)
else:
	print(str2+" != "+str3)

print()
print(values)
if 13 in values or 14 not in values:
	print("Right!")
else:
	print("Wrong!")
	
if 81 in values:
	print("This list include 81")
else:
	print("This list doesnt include 81")
if 14 in values:
	print("This list include 14")
else:
	print("This list doesnt include 14")
