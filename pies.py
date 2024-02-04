import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import random

random.seed(42)
x=np.random.randint(40, size=(6,))
labelss=["bananas","oranges","pears","guavas","apples","carrots"]
plt.pie(x, labels=labelss)
plt.show()