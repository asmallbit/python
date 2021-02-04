user_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'fermi'}
	
players ={
	'john': 'america',
	'luke': 'england',
	'mike': 'australia',
	'amy': 'japan',
	'bill': 'america'}

#遍历所有的键-值对
for key, value in user_0.items():
	print("Key: "+key)
	print("Value: "+value)
	print()

#遍历字典中的所有键
for name in players.keys():		#也可直接写成	for name in players:
	print(name.title())

for name in players:
	print("Hi "+name.title()+", are you from "+players[name].title()+"?")

print()
#按顺序遍历字典中的所有键
for name in sorted(players.keys()):
	print(name.title()+", Thank you for play this game!")

print()
#遍历字典中的所有值
print("The following countries have been mentioned:")
for country in sorted(players.values()):
	print(country.title())
print()
#剔除重复项,可使用set()
for country in sorted(set(players.values())):
	print(country.title())
