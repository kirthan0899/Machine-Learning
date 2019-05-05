import numpy as np
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4],[1, 4, 9, 16],"b--")
plt.show()


plt.plot([1, 2, 3, 4],[1, 4, 9, 16],"g--")
plt.show()


plt.plot([1, 2, 3, 4],[1, 4, 9, 16],"go")
plt.show()



plt.plot([1, 2, 3, 4],[1, 4, 9, 16],"g^")
plt.show()

plt.plot([1, 2, 3, 4],[1, 4, 9, 16],"kD")
plt.show()

plt.plot([1, 2, 3, 4],[1, 4, 9, 16],"kD--")
plt.show()

x = np.arange(1,5)
y = x**3
plt.plot([1, 2, 3, 4],[1, 4, 9, 16],"kD--",x,y,"go")
plt.show()

x = np.arange(1,5)
y = x**3
plt.subplot(1,2,1)
plt.plot([1,2,3,4],[1,4,9,16])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()

x = np.arange(1,5)
y = x**3
plt.subplot(2,1,1) #plt.subplot(nrows, ncols, index)
plt.plot([1,2,3,4],[1,4,9,16])
plt.subplot(2,1,2)
plt.plot(x,y,"gD")
plt.show()

