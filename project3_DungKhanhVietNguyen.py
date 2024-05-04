# Dung K.V. Nguyen (1607859)

# 1. Problem #4 on page 73
#       Write a function my_split_matrix(m), where m is an array, the output is a list [m1, m2] where m1 is
#       the left half of m, and m2 is the right half of m. In the case where there is an odd number of columns,
#       the middle column should go to m1

# 2.  Problem #13 on page 75
#       Write a function my_within_tolerance(A, a, tol) where the output is an array or list of the
#       indices in A such that |A −a| <tol. Assume that A is a one-dimensional float list or array, and that
#       a and tol are 1 by 1 floats.

import numpy as np


def my_split_matrix(m):
    row, col = m.shape
    wall = ((col // 2) + (col % 2))
    p1 = m[:row, :wall]
    p2 = m[:row, wall:]
    return p1, p2


def my_within_tolerance(A, a, tol):
    indices_list = []
    for i in range(len(A)):
        if abs(A[i] - a) < tol:
            indices_list.append(i)
    return indices_list


print("Problem 1")
# Testcase 1
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m1, m2 = my_split_matrix(m)
print(f"{m1}\n")
print(f"{m2}\n")
# Testcase 2
m = np.ones((5, 5))
m1, m2 = my_split_matrix(m)
print(f"{m1}\n")
print(f"{m2}\n")

print("Problem 2")
test1 = my_within_tolerance([0, 1, 2, 3], 1.5, 0.75)
test2 = my_within_tolerance(np.arange(0, 1.01, 0.01), 0.5, 0.03)
print(f"{test1}")
print(f"{test2}")
