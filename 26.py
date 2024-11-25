import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [2, 4, 6, 8]
plt.subplot(1, 2, 1)
plt.plot(x, y1, label="Line 1", color="blue")
plt.title("Plot 1")
plt.subplot(1, 2, 2)
plt.plot(x, y2, label="Line 2", color="green")
plt.title("Plot 2")
plt.tight_layout()
plt.show()
