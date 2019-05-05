import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 15*np.pi, 0.1)
y = np.sin(x)
plt.xlim(0,50)
plt.ylim(-1,1)
plt.title("Sine Wave")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
plt.show()