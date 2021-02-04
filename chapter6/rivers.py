rivers={'nile': 'egypt',
	'amazon': 'brazil',
	'yangtze': 'china'}
	
for river in rivers:
	print("The "+river.title()+" runs through "+rivers[river].title())
	
print()
for river in rivers:
	print(river.title())

print()
for river in rivers:
	print(rivers[river].title())
