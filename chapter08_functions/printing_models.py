from printing_functions import print_models, show_completed_models

#首先创建一个列表,其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#模拟打印每个设计,直到没有打印的设计为止
#	打印每个设计后,都将其移到列表completed_models中
while unprinted_designs:
	current_design = unprinted_designs.pop()
	
	#模拟根据设计制作3D打印模型的过程
	print("Printing model: " + current_design)
	completed_models.append(current_design)
	
#显示打印的所有模型
print("\nThe following models have been printed: ")
for completed_model in completed_models:
	print(completed_model)

print()
#改编 函数见printing_functions.py

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print()
#禁止函数修改列表 将列表的副本传递给函数
#function_name(list_name[:])
#切片表示法[:]创建列表的副本.示例
unprinted_designs = ['desk','computer','poco phone']
completed_models = []
#创建列表副本并以列表副本作为参数
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print("The unprinted_designs list is: "+str(unprinted_designs))
