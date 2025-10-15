import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([1, 2, 3])
x2 = np.array([3, 4, 7])
y = np.array([2,5,9])

X = np.array([
    [1, x1[0], x2[0]],
    [1, x1[1], x2[1]],
    [1, x1[2], x2[2]]
])
Y = y.reshape(-1, 1)

Xt = X.T

# formula b^ = ((X*Xt)^-1 * Xt)Y
beta = np.linalg.inv(Xt @ X) @ Xt @ Y

print("Intercept :", beta[0][0])
print("Coefficient X1:", beta[1][0])
print("Coefficient X2:", beta[2][0])

Y_pred = X @ beta
print("Predicted Y:", Y_pred)