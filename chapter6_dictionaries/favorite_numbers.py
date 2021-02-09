favorite_numbers={'Bob':'34',
	'Taylor':'45',
	'Amy':'2',
	'Lucy':'43',
	'Jill':'3'}
for person_favorite_number in favorite_numbers:
	print(person_favorite_number +"'s favorite number is "+favorite_numbers[person_favorite_number]+".")

print()

for key, value in favorite_numbers.items():
	print(key+"'s favorite number is "+value+".")

############################################################
print()
print("**********************************************")
favorite_numbers={'Bob':['34','100','19'],
	'Taylor':['34','23','45'],
	'Amy':['2','3','15'],
	'Lucy':['43'],
	'Jill':['45','2','3']}
for name,favorite_number in favorite_numbers.items():
	if len(favorite_number)==1:
		print(name.title()+"'s favorite number is:\n\t"+favorite_number[0]+"\n")
	else:
		print(name.title()+"'s favorite number are:")
		for number in favorite_number:
			print("\t"+number)
		print()
