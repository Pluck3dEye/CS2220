# Dung K.V. Nguyen (1607859)
import numpy as np


# Problem #3 page 102
def my_n_max(x, n):
    result = []
    for e in range(n):
        largest = max(x)
        result.append(largest)
        x.remove(largest)
    return result


x = [7, 9, 10, 5, 8, 3, 4, 6, 2, 1]
n = 3
print(f"# Problem #3 page 102")
print(f"{my_n_max(x, n)}\n")


# Problem #5 page 102
def my_mat_mult(P, Q):
    P = np.array(P)  # P : m x p array.
    Q = np.array(Q)  # Q : p x n array.

    m, p = P.shape
    _p, n = Q.shape
    # p = _p

    result = [[0] * n for e in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(p):
                result[i][j] += P[i, k] * Q[k, j]
    return result


def print_result(result):
    for row in result:
        print(row)


print("# Problem #5 page 102")
print("Testcase 1:")
P = np.ones((3, 3))
print_result(my_mat_mult(P, P))

print("\nTestcase 2:")
P = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
Q = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
print_result(my_mat_mult(P, Q))
