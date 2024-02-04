import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import random

random.seed(42)
x=np.random.randint(40, size=(6,))
labelss=["bananas","oranges","pears","guavas","apples","carrots"]
wedge_colors=["hotpink", "blue", "black", "yellow","grey","green"]
explode_values=[0.1,0.1,0.1,0.1,0.1,0.1]
plt.pie(x, labels=labelss, startangle=90, explode=explode_values, shadow=True, colors=wedge_colors)
plt.show()