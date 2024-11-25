import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color='green')
plt.title('Scatter Graph (Random Distribution)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
