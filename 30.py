import numpy as np
import matplotlib.pyplot as plt
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]
x = np.arange(len(labels))  
width = 0.35  
fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, men_means, width, label="Men")
bars2 = ax.bar(x + width/2, women_means, width, label="Women")
ax.set_xlabel("Groups")
ax.set_ylabel("Scores")
ax.set_title("Scores by Group and Gender")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.show()
