##将函数存储在模块中
##1.导入整个模块 import module_name		使用module_name.function_name()可调用导入模块中的任何一个函数
#import pizza
#pizza.make_pizza2(16,'pepperoni')
#pizza.make_pizza2(12,'mushroom','green peppers','extra cheese')

################################################################

#2.导入特定函数 from module_name import function_name0, function_name1, function_name2
#使用function_name0, function_name1......即可调用导入的函数
from pizza import make_pizza2
make_pizza2(16,'pepperoni')
make_pizza2(12,'mushroom','green peppers','extra cheese')

#使用as给函数或模块指定别名
#函数		from module_name import function_name as ...(要指定的别名)
#模块		import module_name as ...(要指定的别名)

#导入模块中的所有函数
#from module_name import *
