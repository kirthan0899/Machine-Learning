import numpy as np
import matplotlib.pyplot as plt

div = (['A','B','C','D','E'])
avg_marks = (70,80,84,67,20)
plt.bar(div,avg_marks,color="green")
plt.show()

div = (['A','B','C','D','E'])
avg_marks = (70,80,84,67,20)
plt.barh(div,avg_marks,color="green") #barh for horizontal graph
plt.show()

Branch = ['CS','ECE','ME','IS','CE']
strength = [150,200,120,66,40]
plt.pie(strength)

Branch = ['CS','ECE','ME','IS','CE']
strength = [150,200,120,66,40]
plt.pie(strength, labels=Branch, shadow=True, startangle=90)

Branch = ['CS','ECE','ME','IS','CE']
strength = [150,200,120,66,40]
Explode=(0.1,0,0.2,0.5,0)
plt.pie(strength, labels=Branch, shadow=True, explode=Explode, startangle=90)

Branch = ['CS','ECE','ME','IS','CE']
strength = [150,200,120,66,40]
Explode=(0.1,0,0.6,0.5,1)
plt.pie(strength, labels=Branch, explode=Explode)