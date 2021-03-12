bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
#output is trek
print(bicycles[0].title())
print(bicycles[-1])
#将索引指定为-1后,python会返回最后一个列表元素,-2返回倒数第二个元素,以此类推
message = "My first bicycle was a "+bicycles[0].title()+"."
print(message)
