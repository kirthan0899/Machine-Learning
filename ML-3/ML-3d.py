# Scatter plot
import numpy as np
import matplotlib.pyplot as plt

height = [170, 166, 153, 100, 90, 133, 165, 170, 159, 180]
weight = [55, 65, 75, 89, 35, 20, 90, 67, 89, 24]
plt.xlim(90, 200)
plt.ylim(20, 100)
plt.xlabel("Height-->")
plt.ylabel("Weight-->")
plt.title("Graph-2")
plt.scatter(height, weight, color="red")
plt.show()

Branch = ['CS','ECE','ME','IS','CE']
strength = [150,200,120,66,40]
Explode=(0.1,0,0.2,0.5,0)
plt.pie(strength, labels=Branch, shadow=True, explode=Explode, startangle=90)
plt.legend(title="TEST")