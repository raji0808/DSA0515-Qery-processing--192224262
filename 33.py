import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, edgecolor='black', facecolor='none')
plt.title('Scatter Plot with Empty Circles')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
