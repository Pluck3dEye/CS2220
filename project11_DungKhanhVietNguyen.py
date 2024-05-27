# Dung K.V. Nguyen (1607859)

import numpy as np
from numpy.linalg import norm


# The first #3 page 261
def my_is_orthogonal(v1, v2, tol):
    cos_theta = np.dot(v1.T, v2) / (norm(v1) * norm(v2))
    theta = np.arccos(cos_theta)
    return 1 if np.abs(np.pi/2 - theta) < tol else 0


# The second #3 page 261
def my_is_similar(s1, s2, tol):
    # Get vector from string
    def get_vector(s):
        v = np.zeros((26, 1))
        for c in s.lower():
            if c.isalpha():
                v[ord(c) - ord('a'), 0] += 1
        return v

    v1 = get_vector(s1)
    v2 = get_vector(s2)

    abs_theta = abs(np.arccos(np.dot(v1.T, v2) / (norm(v1) * norm(v2))))
    return 1 if abs_theta < tol else 0


# Test cases for the first #3
print("The first #3 page 261:")
a = np.array([[1], [0.001]])
b = np.array([[0.001], [1]])
# output: 1
print(my_is_orthogonal(a,b, 0.01))
# output: 0
print(my_is_orthogonal(a,b, 0.001))

a = np.array([[1], [0.001]])
b = np.array([[1], [1]])
# output: 0
print(my_is_orthogonal(a,b, 0.01))

a = np.array([[1], [1]])
b = np.array([[-1], [1]])
# output: 1
print(my_is_orthogonal(a,b, 1e-10))

# Test case for the second #3
print("\nThe second #3 page 261:")
string_1 = "Nobody loves a pig wearing lipstick."
string_2 = "Knowing is not enough, we must apply. Willing is not enough, we must do."
print(my_is_similar(string_1, string_2, 0.7))
print(my_is_similar(string_1, string_2, 0.5))
