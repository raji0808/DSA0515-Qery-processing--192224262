import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 1000  
plt.scatter(x, y, s=sizes, alpha=0.5, color='purple')
plt.title('Scatter Plot with Balls of Different Sizes')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
