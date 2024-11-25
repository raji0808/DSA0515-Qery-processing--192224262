import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [2, 4, 6, 8]
plt.plot(x, y1, label="Line 1", linewidth=2, color="blue")
plt.plot(x, y2, label="Line 2", linewidth=3, color="green")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Multiple Lines Example")
plt.legend()
plt.show()
