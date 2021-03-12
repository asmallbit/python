message = 'If you could visit one place in the world, where would you go?'
message += '\nEnter "quit" to end this program.'
loop = True
places=[]
while loop:
	place = input(message)
	if place.lower() != 'quit':
		places.append(place)
	else:
		loop = False

print("All you guys answer is:\n"+str(places))
