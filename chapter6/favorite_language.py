#由类似对象组成的字典
favorite_languages={
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
print("Sarah's favorite language is "+
	favorite_languages['sarah'].title()+".")

#练习6.6
print()
guys=['jen','bob','phil','amy','edward','peter','sarah']
for guy in guys:
	if guy in favorite_languages:
		print("Thanks! "+guy.title())
	else:
		print(guy.title()+", please finish the paper.")
