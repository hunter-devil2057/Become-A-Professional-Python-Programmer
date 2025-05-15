import matplotlib.pyplot as plt
# plt.title("Epic Graph Tutorial for Data visualization in Python with Matplotlib.\nTutorial showing labels and titles")
x = [1, 2, 3, 4, 5]
y = [4, 7, 4, 7, 3]
y2 = [5, 3, 2, 6, 2]

plt.title("Bar Chart Tutorial")
plt.bar(x, y, label = "One", color = "m")
plt.bar(x, y2, label = "Two", color = "g")

plt.xlabel("Bar Number")
plt.ylabel("Bar Height")

plt.legend()
plt.show()