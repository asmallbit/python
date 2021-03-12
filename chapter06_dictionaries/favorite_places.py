#Á·Ï°6-9
favorite_places={'mike':['london','paris'],'jill':['peking'],
	'tom':['shanghai','guangzhou'],'allan':['nyc','london']}
for name,favorite_place in favorite_places.items():
	if len(favorite_place)==1:
		if 'nyc' in favorite_place:
			print(name.title()+"'s favorite palce is\n\t"+favorite_place[0].upper()+"\n")
		else:
			print(name.title()+"'s favorite place is\n\t"+favorite_place[0].title()+"\n")
	else:
		print(name.title()+" likes these places:")
		if 'nyc' in favorite_place:
			for place in favorite_place:
				if place=='nyc':
					print("\t"+place.upper())
				else:
					print("\t"+place.title())
		else:
			for place in favorite_place:
				print("\t"+place.title())
