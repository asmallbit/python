#使用任意数量的关键字实参	**user_info使python创建一个名为user_info的空字典,并将所有收到的键值对都封装到这个字典中
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile0 = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile0)
user_profile1 = build_profile('jw','han',school='computer science',age='21',location='shenzhen')
print(user_profile1)
