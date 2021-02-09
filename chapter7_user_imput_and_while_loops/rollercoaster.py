height=input("How tall are you, in inches?")
height=int(height)

#int()让python将字符串或浮点类型类型转化为数值
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

#python应使用raw_input()获取输入
