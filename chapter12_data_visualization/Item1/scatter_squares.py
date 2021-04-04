import matplotlib.pyplot as plt

#plt.scatter(2, 4)
#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]
x_values2 = list(range(1, 1001))
y_values2 = [x**2 for x in x_values2]
'''
scatter()还可自定义颜色,可将自定义颜色传递给参数c. 用法: 将参数设置为一个元组
其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量。
值越接近0,指定的颜色越深,反之,颜色越浅 eg c=(0, 0, 0.8)
'''
#plt.scatter(x_values2, y_values2, c='red', edgecolor='none', s=10)

'''
将参数c设置成一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。这些代
码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色
'''
plt.scatter(x_values2, y_values2, c=y_values2, cmap=plt.cm.Blues, edgecolors='none', s=40)
#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)
#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.savefig('test_tight.png', bbox_inches='tight')
plt.savefig('test.png')
plt.show()