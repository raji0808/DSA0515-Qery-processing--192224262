import matplotlib.pyplot as plt
x, y = [], []
with open("D:/QP/text.txt", 'r') as file:
    for line in file:
        xi, yi = map(int, line.split())
        x.append(xi)
        y.append(yi)

plt.plot(x, y, label="Data from text file")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line Chart from File")
plt.legend()
plt.show()
