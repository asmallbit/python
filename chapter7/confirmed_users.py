#先创建一个待验证用户列表和一个用于存储已验证的用户的列表
unconfirmed_users=['alice','brain','candace']
confirmed_users=[]
#验证每个用户,直到没有验证用户为止,将每个经过验证的列表都移到已验证用户中
while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	
	print("Verifying user: "+current_user.title())
	confirmed_users.append(current_user)
	
#显示已验证的用户
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
