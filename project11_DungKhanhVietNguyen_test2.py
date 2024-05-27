import numpy as np
from numpy.linalg import norm, det, inv, cond, matrix_rank

# from scipy.linalg import

u = np.array([[4, 3, -5],
[0, -2.5, 2.5],
[0, 0, 12]])
l = np.array([[1, 0, 0],
[-0.5, 1, 0],
[2, -0.8, 1]])
print("LU=", np.dot(l, u))

#  Gauss–Seidel method
#   8(x1)  + 3(x2) − 3(x3)   = 14,
#   −2(x1) − 8(x2) + 5(x3)   = 5,
#   3(x1)  + 5(x2) + 10(x3)  = −8.


a = [[8, 3, -3], [-2, -8, 5], [3, 5, 10]]
# Find diagonal coefficients
diag = np.diag(np.abs(a))
print("Diagonal:", diag)
# Find row sum without diagonal
off_diag = np.sum(np.abs(a), axis=1) - diag
print(off_diag)
if np.all(diag > off_diag):
    print("matrix is diagonally dominant")
else:
    print("NOT diagonally dominant")

x1 = 0
x2 = 0
x3 = 0
epsilon = 0.01
converged = False
x_old = np.array([x1, x2, x3])
print("Iteration results")
print(" k, x1, x2, x3 ")
for k in range(1, 50):
    x1 = (14-3*x2+3*x3)/8
    x2 = (5+2*x1-5*x3)/(-8)
    x3 = (-8-3*x1-5*x2)/(-5)
    x = np.array([x1, x2, x3])
    # check if it is smaller than threshold
    dx = np.sqrt(np.dot(x-x_old, x-x_old))
    print("%d, %.4f, %.4f, %.4f" % (k, x1, x2, x3))
    if dx < epsilon:
        converged = True
        print("Converged!")
        break
    # assign the latest x value to the old value
    x_old = x

if not converged:
    print("Not converged, increase the # of iterations")

# SOLVING SYSTEMS OF LINEAR EQUATIONS IN PYTHON

A = np.array([[4, 3, -5],
[-2, -4, 5],
[8, 8, 0]])
y = np.array([2, 5, -3])
x = np.linalg.solve(A, y)
print(x)
