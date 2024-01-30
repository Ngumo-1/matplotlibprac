import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
x=np.random.rand(50)
y1 = 2 * x + 1 + 0.1 * np.random.randn(50)
y2 = -2 * x + 1 + 0.1 * np.random.randn(50)
plt.scatter(x, y1, color='green', alpha=0.3, )
plt.scatter(y1, y2, color='red', alpha=0.3)
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.legend("XY")
plt.title("Challenge 1: Basic Scatter Plot Customization", loc='center')
plt.show()
# sizes=np.random.randint(100, size=(50))

