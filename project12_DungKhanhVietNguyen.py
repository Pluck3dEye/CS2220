# Dung K.V. Nguyen (1607859)

import numpy as np

A = np.array([[2, 1, 2],
              [1, 3, 2],
              [2, 4, 1]])

e_value, e_vector = np.linalg.eig(A)

print("E-value:\n", e_value)
print("E-vector:\n", e_vector)