import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)
plt.title("My Graph")
plt.hist(x)
plt.show()

x = np.random.randn(1000)
plt.title("My Graph-1")
plt.hist(x, 20, color="red")
plt.show()