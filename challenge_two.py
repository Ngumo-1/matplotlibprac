import numpy as np
import matplotlib.pyplot as plt


# Generating synthetic dataset for Challenge 2
np.random.seed(456)
x = np.random.rand(50)
y = np.random.rand(50)
color_variable = np.random.rand(50)  # Use this for coloring each dot individually
size_variable = 100 * np.random.rand(50)
alpha_variable = 0.5 + 0.5 * np.random.rand(50)
color_map=np.random.randint(100, size=(100))

plt.scatter(x, y, c=color_variable, s=size_variable, alpha=alpha_variable, cmap='viridis')
plt.colorbar()
plt.grid(alpha=0.7, ls='--')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

plt.title("Challenge 2: Advanced Scatter Plot Customization", loc='center')
plt.show()