import matplotlib.pyplot as plt
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.barh(languages, popularity, color="lightgreen")
plt.xlabel("Popularity (%)")
plt.ylabel("Programming Languages")
plt.title("Popularity of Programming Languages (Horizontal)")
plt.show()
