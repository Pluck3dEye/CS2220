
# Linear Regression

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

plt.style.use('ggplot')

x = np.linspace(0, 1, 101)

y = 1 +x + x * np.random.random(len(x))

# print(x)
# print(y)

A = np.vstack([x, np.ones(len(x))]).T

print(A)

y = y[:, np.newaxis]

print(y)

alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
print("Alpha:\n", alpha)

plt.figure(figsize = (10,8))
plt.plot(x, y, "b.")
# plt.plot(x, alpha[0]*x + alpha[1], "r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()