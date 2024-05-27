import numpy as np
vector_row = np.array([[1,2,3]])
vector_column = np.array([[1],[2],[3],[4]])
print(vector_row.shape)
print(vector_column.shape)

from numpy.linalg import norm

new_vector = vector_row
print(new_vector)
norm_1 = norm(new_vector, 1)
norm_2 = norm(new_vector, 2)
norm_inf = norm(new_vector, np.inf)
print("L_1 is: %.1f"%norm_1)
print("L_2 is: %.1f"%norm_2)
print("L_inf is: %.1f"%norm_inf)

new_vector = vector_row.T
print(new_vector)
norm_1 = norm(new_vector, 1)
norm_2 = norm(new_vector, 2)
norm_inf = norm(new_vector, np.inf)
print("L_1 is: %.1f"%norm_1)
print("L_2 is: %.1f"%norm_2)
print("L_inf is: %.1f"%norm_inf)

new_vector = np.array([1,2,3])
print(new_vector)
norm_1 = norm(new_vector, 1)
norm_2 = norm(new_vector, 2)
norm_inf = norm(new_vector, np.inf)
print("L_1 is: %.1f"%norm_1)
print("L_2 is: %.1f"%norm_2)
print("L_inf is: %.1f"%norm_inf)
