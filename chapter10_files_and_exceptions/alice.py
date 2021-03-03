def count_words(filename):
	'''计算一个文件大致包含多少单词'''
	try:
		with open(filename, encoding='UTF-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#msg = 'Sorry, the file '+filename+" does not exist."
		#print(msg)
		pass
		#pass 是空语句,是为了保持程序结构的完整性.pass不做任何事情,一般用来做占位语句
	else:
		#计算文件大致包含多少单词
		words = contents.split()
		num_words = len(words)
		file_name = str(filename).replace('resource/','')
		print("The file "+file_name+" has about "+str(num_words)+" words.")
		
#考虑转义字符'\a'为响铃,此处用'/'
filename = 'resource/alice.txt'
count_words(filename)
print()
filenames=['resource/alice.txt', 'resource/siddhartha.txt', 'resource/moby_dick.txt', 'resource/little_women.txt','human.txt']
for filename in filenames:
	count_words(filename)
#相关链接
#https://blog.csdn.net/qq_33363973/article/details/77862007
#split()以空格将字符串分割为多个部分,并存储到一个列表中.
