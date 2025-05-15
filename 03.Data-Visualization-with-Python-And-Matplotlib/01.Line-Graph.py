import matplotlib.pyplot as plt
plt.title("Epic Graph Tutorial for Data visualization in Python with Matplotlib.\nTutorial showing labels and titles")
x = [1, 2, 3, 4, 5]
y = [4, 7, 4, 7, 3]
y2 = [5, 3, 2, 6, 2]
# plt.plot([1, 2, 3, 4, 5], [4, 5, 6, 7, 3])
plt.xlabel("Plot Number")
plt.ylabel("Random #")
plt.plot(x, y, label = "y")
plt.plot(x, y2, label = "y2")
plt.legend()
plt.show()
print("Got Here...")