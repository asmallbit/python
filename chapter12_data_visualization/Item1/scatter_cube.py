import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolors='none', s=10)
plt.title("Cube Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=14)
plt.axes =([0, 5100, 0, 5100**2])
plt.show()
