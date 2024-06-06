from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
#
# x_ = 0.5
# x = np.array([0, 1, 2])
# y = np.array([1, 3, 2])
# f = interp1d(x, y)
# y_hat = f(x_)
# print(y_hat)
#
# plt.figure(figsize=(10, 8))
# plt.plot(x, y, "-ob")
# plt.plot(x_, y_hat, "ro")
# plt.title("Linear Interpolation at x = 1.5")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

b = np.array([1, 3, 3, 2, 0, 0, 0, 0])
b = b[:, np.newaxis]
A = np.array([[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 8, 4, 2, 1],
[3, 2, 1, 0, -3, -2, -1, 0],
[6, 2, 0, 0, -6, -2, 0, 0],
[0, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 12, 2, 0, 0]])

result = np.dot(np.linalg.inv(A), b)
print(result)
