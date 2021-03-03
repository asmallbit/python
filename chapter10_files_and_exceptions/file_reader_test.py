#练习10-1 & 10-2
filename = 'resource\programming.txt'
with open(filename) as file_object:
	first = file_object.read()
	print(first)

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip()) 

with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	#replace可将字符串中的特定字符序列替换为其他字符序列
	print(line.replace('love','hate').rstrip())
