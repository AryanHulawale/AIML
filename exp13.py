import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 2, 4, 5, 4, 7])

Mean_of_x = np.mean(x)
Mean_of_y = np.mean(y)

num = ((x-Mean_of_x)*(y-Mean_of_y))
den = ((x-Mean_of_x)**2)

m = np.sum(num) / np.sum(den) 

b = Mean_of_y - m*Mean_of_x

Prediction= m*x + b

plt.scatter(x,y, color='blue', label='Actual data')
plt.plot(x,Prediction , color='red', label='Regression line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
