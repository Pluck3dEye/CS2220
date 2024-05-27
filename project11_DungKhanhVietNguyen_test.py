import numpy as np
from numpy.linalg import norm, det, inv, cond, matrix_rank


# vector_row = np.array([[1, -5, 3, 2, 4]])
# vector_column = np.array([[1], [2], [3], [4]])
# print(vector_row.shape)
# print(vector_column.shape)
#
# new_vector = vector_row.T
# print(new_vector)
# norm_1 = norm(new_vector, 1)
# norm_2 = norm(new_vector, 2)
# norm_inf = norm(new_vector, np.inf)
#
# print(norm_1)
# print("%.1f" % norm_2)
# print(norm_inf)
#
# add_vector = vector_row * vector_column
# print(add_vector)
# add_vector = 2 * vector_column
# print(add_vector)
# add_vector = vector_row - vector_column
# print(add_vector)
#
# # dot-product
# v = np.array([[10, 9, 3]])
# w = np.array([[2, 5, 12]])
# theta = np.arccos(np.dot(v, w.T) / (norm(v) * norm(w)))
# print(theta)
#
# # cross-product
# # v × w = ||v||2 ||w||2 sin(θ) n
# v = np.array([[0, 2, 0]])
# w = np.array([[3, 0, 0]])
# print(np.cross(v, w))
# # linear combination
#
# v = np.array([[0, 3, 2]])
# w = np.array([[4, 1, 1]])
# u = np.array([[0, -2, 0]])
# x = 3*v-2*w+4*u
# print(x)

# M = np.array([[0, 2, 1, 3],
#               [3, 2, 8, 1],
#               [1, 0, 0, 3],
#               [0, 3, 2, 1]])
# print("M:\n", M)
# print("Determinant: %.1f" % det(M))
# I = np.eye(4)
# print("I:\n", I)
# print("M*I:\n", np.dot(M, I))
#
# print("Inv M:\n", inv(M))
# P = np.array([[0, 1, 0],
#               [0, 0, 0],
#               [1, 0, 1]])
# print("det(p):\n", det(P))
#
# A = np.array([[1, 1, 0],
#               [0, 1, 0],
#               [1, 0, 1]])
# print("Condition number:\n", cond(A))
# print("Rank:\n", matrix_rank(A))
# y = np.array([[1], [2], [1]])
# A_y = np.concatenate((A, y), axis=1)
# print("Augmented matrix:\n", A_y)


def my_is_similar(s1, s2, tol):
    # Get vector from string
    def get_vector(s):
        v = np.zeros(26)
        for c in s.lower():
            if c.isalpha():
                v[ord(c) - ord('a')] += 1
        return v

    v1 = get_vector(s1)
    v2 = get_vector(s2)
    print(v1)
    print(v2)
    abs_theta = abs(np.arccos(np.dot(v1, v2) / (norm(v1) * norm(v2))))
    print(abs_theta)

    v1 = get_vector(s1).reshape(1, -1)
    v2 = get_vector(s2).reshape(-1, 1)
    print(v1)
    print(v2)
    abs_theta = abs(np.arccos(np.dot(v1, v2) / (norm(v1) * norm(v2))))
    print(abs_theta)

    return 1 if abs_theta < tol else 0


string_1 = "Nobody loves a pig wearing lipstick."
string_2 = "Knowing is not enough, we must apply. Willing is not enough, we must do."
print(my_is_similar(string_1, string_2, 0.5))

arr = np.zeros((26, 1))
print(arr)
