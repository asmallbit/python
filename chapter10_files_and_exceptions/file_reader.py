
with open('resource\pi_digits.txt') as file_object:
	#读取整个文件		contents = file_object.read()
	#将文件内各行存储到某一变量中
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print()

#可将读取的文件名称(路径)存储到其他变量中,如下
file_name = 'resource\pi_digits.txt'
with open(file_name) as file_object:
	#逐行读取
	for line in file_object:
		#每行(line)末尾都有一个换行符,可使用retrip()去掉末尾多余换行符
		print(line.rstrip())
print()
'''
使用关键词with时,open()返回的文件对象只在with代码块中可用.如果要在with代码块外访问文件的
内容,可在with代码块内将文件的各行存储在一个列表中,并在with代码块中使用该列表
读取文本文件时,python将其中的所有文本都解读为字符串.如果读取的是数字,并且要将其作为数值使用,
就必须使用函数int()将其转换为整数,或使用函数float()将其转换为浮点数
'''

#包含一百万字符的大文件 对于可处理的数字量,python没有限制,只要系统内存足够多,便可处理任意多的数据
filename = 'resource\pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()
	
print(pi_string[:50] + '...')
print(len(pi_string))

birthday = input("enter your birthaday, in the yymmdd: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday doesnt appear in the first million digits of pi.")
