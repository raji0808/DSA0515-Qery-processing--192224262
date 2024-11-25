import matplotlib.pyplot as plt
import numpy as np
group1 = {'height': np.random.randint(150, 180, 10), 'weight': np.random.randint(50, 80, 10)}
group2 = {'height': np.random.randint(160, 190, 10), 'weight': np.random.randint(60, 90, 10)}
group3 = {'height': np.random.randint(170, 200, 10), 'weight': np.random.randint(70, 100, 10)}
plt.scatter(group1['height'], group1['weight'], color='blue', label='Group 1')
plt.scatter(group2['height'], group2['weight'], color='green', label='Group 2')
plt.scatter(group3['height'], group3['weight'], color='red', label='Group 3')
plt.title('Weights vs Heights for Three Groups')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.grid(True)
plt.show()
