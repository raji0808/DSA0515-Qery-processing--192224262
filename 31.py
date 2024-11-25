import matplotlib.pyplot as plt
import numpy as np
men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]
men_std = [4, 3, 4, 1, 5]
women_std = [3, 5, 2, 3, 3]
x = np.arange(len(men_means))  
width = 0.35
plt.bar(x, men_means, width, yerr=men_std, label='Men', color='blue')
plt.bar(x, women_means, width, yerr=women_std, label='Women', bottom=men_means, color='orange')
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender with error bars')
plt.xticks(x)
plt.legend()
plt.show()
