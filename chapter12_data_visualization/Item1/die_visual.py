from die import Die
import pygal
import matplotlib.pyplot as plt 

#添加标签
def add_labels(min, max):
    labels = []
    for value in range(min, max+1):
        labels.append(value)
    return labels

#创建两个骰子
die1 = Die()
die2 = Die()
die3 = Die()

#掷骰子
results = []
for roll_num in range(1000):
    end_result = die1.roll() + die2.roll() + die3.roll()
    results.append(end_result)

frequencies = []
max_result = die1.num_sides + die2.num_sides +die3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

'''
#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling three D6 1000 times."
hist.x_labels = add_labels(3, max_result)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6 ', frequencies)
hist.render_to_file('die_visual.svg')
'''

plt.bar(add_labels(3, max_result), frequencies)
plt.title("Results of rolling two D6 in 1000 times.")
plt.xlabel("Result", fontsize=15)
plt.ylabel("Frequency of Result", fontsize=15)
plt.show()