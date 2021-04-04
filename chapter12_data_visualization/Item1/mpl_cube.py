import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.plot(x_values, y_values, linewidth=5)
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()