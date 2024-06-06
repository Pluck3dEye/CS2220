import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# generate x and y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
print(y)

# assemble matrix A
A = np.vstack([x, np.ones(len(x))]).T
# print(A)

# turn y into a column vector
y = y[:, np.newaxis]
# Direct least squares regression
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), y)
print(alpha)

#
# # plot the results
# plt.figure(figsize = (10,8))
# plt.plot(x, y, "b.")
# plt.plot(x, alpha[0]*x + alpha[1], "r")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()
