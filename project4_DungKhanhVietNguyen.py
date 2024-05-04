# Dung K.V. Nguyen (1607859)

import numpy as np
import math


# Problem #4 page 86
def my_make_size10(x):
    if len(x) >= 10:
        return list(x)[:10]
    else:
        x = list(x) + [0] * (10 - len(x))  # or  x + [0 for e in range(10-len(x))]
        return x


print("Problem #4 page 86")
test_1 = my_make_size10(range(1, 3))
test_2 = my_make_size10(range(1, 15))
print(f"Test Case 1: {test_1}")
print(f"Test Case 2: {test_2}\n")

# Problem #5 page 87
# def my_make_size10(x):
#     x = (list(x) + [0] * (10 - len(x)))[:10]
#     return x

# Problem #8 page 88
def my_n_roots(a, b, c):
    n_roots = 0
    r = []
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        n_roots += 2
        r.append((-b + math.sqrt(delta)) / (2 * a))
        r.append((-b - math.sqrt(delta)) / (2 * a))
    elif delta < 0:
        n_roots += -2
        real = -b / (2 * a)
        imaginary = math.sqrt(abs(delta)) / (2 * a)
        r.append(complex(real, imaginary))
        r.append(complex(real, -imaginary))
    else:
        n_roots += 1
        r.append(-b / (2 * a))
    return n_roots, r


# Another solution using np.roots() to solve polynomial f
# def my_n_roots(a, b, c):
#     coefficients = [a, b, c]
#     delta = b ** 2 - 4 * a * c
#     if delta > 0:
#         n_roots = 2
#     elif delta < 0:
#         n_roots = 1
#     else:
#         n_roots = 0
#     r = np.roots(coefficients)
#     return n_roots, r

print("Problem #8 page 88")
n_roots, r = my_n_roots(1, 0, -9)
print(f"Test Case 1:\n{n_roots}\n{r}\n")
n_roots, r = my_n_roots(3, 4, 5)
print(f"Test Case 2:\n{n_roots}\n{r}\n")
n_roots, r = my_n_roots(2, 4, 2)
print(f"Test Case 3:\n{n_roots}\n{r}\n")
