import matplotlib.pyplot as plt
from random_walk import RandomWalk
import pygal

'''
#scatter version
while True:
    #创建一个RandomWalk实例,并将其包含的点绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()
    #设置绘图窗口的尺寸,单位为英寸
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    #突出起点与终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.title('Random Walk', fontsize=25)
    #隐藏坐标轴
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    plt.show()
    flag = input("Do you want to make another walk? (y/n): ")
    if flag.lower()=='n':
        break
'''

'''
#mpl version
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.tick_params(axis='both', labelsize=10)
    plt.show()

    flag = input("Do you want to make another walk? (y/n): ")
    if flag.upper()=='N':
        break
'''

#pygal version
rw = RandomWalk(5000)
rw.fill_walk()
line_chart = pygal.Line()
line_chart.add('random',rw.y_values)
line_chart.render_to_file("rw_visual.svg")