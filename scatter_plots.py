import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(123)
# x=np.random.rand(50)
# y1 = 2 * x + 1 + 0.1 * np.random.randn(50)
# y2 = -2 * x + 1 + 0.1 * np.random.randn(50)
# plt.scatter(x, y1, color='green', alpha=0.3, label='Dataset 1')
# plt.scatter(y1, y2, color='red', alpha=0.3, label='Dataset 1')
# plt.ylabel('Y-axis')
# plt.xlabel('X-axis')
# plt.legend("XY")
# plt.title("Challenge 1: Basic Scatter Plot Customization", loc='center')
# plt.show()
# sizes=np.random.randint(100, size=(50))

np.random.seed(42)
arr1=np.random.randint(40, size=(20))
arr2=np.random.randint(40, size=(20))
plt.scatter(arr1, arr2, color="hotpink", marker="*")

x=np.random.randint(30, size=15)
y=np.random.randint(30, size=15)
plt.scatter(x, y, color="blue", marker="o")

plt.show()

