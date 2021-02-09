citys = ["Tokyo", "London", "NYC", "HK", "Paris", "Peking"]
print("I love these citys\n"+str(citys))
sorted_citys = sorted(citys)
print(sorted_citys)
print("The original city is:" +str(citys))
#元素顺序反转 reverse()方法
citys.reverse()
print(citys)
#元素顺序再次反转,即回到反转前的状态
citys.reverse()
print(citys)
#使用sort()修改该列表
citys.sort()
print("After use sort() function:")
print(citys)

