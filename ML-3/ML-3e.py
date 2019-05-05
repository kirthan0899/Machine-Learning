import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
height=([130,140,156,125,146,135,155,190])
weight=([50,65,80,66,52,45,90,88])
ax=plt.axes(projection='3d')
ax.scatter(height,weight)

height=([130,140,156,125,146,135,155,190])
weight=([50,65,80,66,52,45,90,88])
ax=plt.axes(projection='3d')
ax.plot(height,weight)

x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()