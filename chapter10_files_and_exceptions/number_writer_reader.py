#存储数据
import json

numbers = [2,3,5,56,54,34,13456]

filename = 'resource/numbers.json'
with open(filename, 'w') as f_obj:
	#json.dump()	接受两个参数,分别是要存储的数据以及用于存储数据的文件对象
	json.dump(numbers, f_obj)
	
with open(filename, 'r') as f_obj:
	#json.load()	接受一个参数,为要加载之前存储的数据的文件对象
	numbers = json.load(f_obj)

print(numbers)
