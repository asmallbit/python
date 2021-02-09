'''
def get_formatted_name(first_name, last_name):
	#返回整洁的姓名
	full_name = first_name + " " + last_name
	return full_name.title()
	
musician = get_formatted_name('jimi','hendrix')
print(musician)
'''
#实参变为可选
def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:		#python将非空字符串解读为True
		full_name = first_name + " " + middle_name + " " + last_name
	else:
		full_name = first_name + " " + last_name
	return full_name.title()
	
musician = get_formatted_name('jimi','hendrix')
print(musician)

print()
musician = get_formatted_name('john','hooker','lee')
print(musician)

#返回字典
def build_person(first_name, last_name, age=''):
	#返回一个字典,其中包含有关一个人的信息
	person = {'first': first_name.title(), 'last': last_name.title()}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix',12)
print(musician)
loop = True
f_name=''
m_name=''
l_name=''
while loop:
	print("\nPlease tell me your name")
	print("Enter quit to end the program.")
	f_name = input('first name: ')
	if f_name.lower() == 'quit':
		break
	m_name = input('middle name: ')
	if m_name.lower() == 'quit':
		break
	l_name = input('last name: ')
	if l_name.lower() == 'quit':
		break
	name = get_formatted_name(f_name,l_name,m_name)
	print("\nHello, "+name+"!")

