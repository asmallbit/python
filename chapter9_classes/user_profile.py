#练习9-3 &　9-5 &　9-7 & 9-8
class User():
	def __init__(self, first_name, last_name, **other_infos):
		self.user={}
		self.user['first_name'] = first_name
		self.user['last_name'] = last_name
		self.user['log_attempts'] = 0
		for key, value in other_infos.items():
			self.user[key] = value
	def increment_login_attempts(self):
		self.user['log_attempts'] += 1
		
	def reset_login_attempts(self):
		self.user['log_attempts'] = 0	
		
	def describe_user(self):
		print("\nAll this guy info is:\n"+str(self.user)+"\n")
	
	def greet_user(self):
		print("Hi, there! "+self.user['first_name'].title()+" "+self.user['last_name'].title())
		
class Admin(User):
	def __init__(self, first_name, last_name, **other_infos):
		super().__init__(first_name, last_name, **other_infos)
		self.privileges = Privileges()
	
	'''	
	def set_privileges(self):
		for privilege in privileges:
			self.privileges.append(privilege)
	
	def show_privileges(self):
		message = "Admin can do this action:\n\t"
		message += str(self.privileges)
		print(message)
	'''
	
class Privileges():
	def __init__(self):
		self.privileges = []
		
	def set_privileges(self, *privileges):
		for privilege in privileges:
			self.privileges.append(privilege)
			
	def show_privileges(self):
		message = "Admin can do this action:\n\t"
		message += str(self.privileges)
		print(message)
	
my_user = User('jwei','han',location='nanking')
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.describe_user()
my_user.greet_user()

test_user = User('john','smith',country='england',sex='boy')
test_user.increment_login_attempts()
test_user.describe_user()
test_user.reset_login_attempts()
test_user.describe_user()
test_user.greet_user()
print()

my_admin = Admin('tim','cook',sex='male')
my_admin.greet_user()
my_admin.privileges.set_privileges('can add post','can deldte post','can be user')
my_admin.privileges.show_privileges()
