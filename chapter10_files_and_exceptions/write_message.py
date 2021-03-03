filename = 'resource/programming.txt'
#open()第二个实参表示以写入模式打开文件.所有模式:读取模式'r',写入模式'w'(会覆盖原有文本),附加模式'a',同时进行读取和写入'r+'
with open(filename, 'w') as file_object:
	#写入多行时,要自行添加换行符,write()函数并不会在写入的文本末尾添加换行符
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")
#python只能将字符串写入文本文件.要将数值数据存储到文本文件中,必须先使用函数str()将其转换为字符串格式

#附加到文件,即保留原文件内容,而非覆盖  参数'a'为附加模式
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
