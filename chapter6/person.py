#Á·Ï°
person_0={'first_name': 'jwei',
	'last_name': 'han',
	'age': '20',
	'city': 'nanking'
}
print("This guy is "+person_0['first_name'].title()+" "+person_0['last_name'].title()+". He is "+
	person_0['age']+" years now. "+"He lives in "+person_0['city'].title()+" now.")
print()
#Á·Ï°6-7
person_1={'first_name':'Matin',
	'last_name':'king',
	'age':'39',
	'city': 'atlanta'}
	
person_2={'first_name':'luyao',
	'last_name':'dong',
	'age':'19',
	'city':'xingtai'}
persons=[person_0,person_1,person_2]
for person in persons:
	print("This guy is "+person['first_name'].title()+" "+person['last_name'].title()+". He/She is "+
	person['age']+" years now. "+"He/She lives in "+person['city'].title()+" now.")
