# Dung K.V. Nguyen (1607859)

# Problem #4 on page 116
def n_factorial(n):
    if n == 0:
        return 1
    return n * n_factorial(n - 1)


def my_n_choose_k(n, k):
    out = int(n_factorial(n) / (n_factorial(k) * n_factorial(n - k)))
    return out


# Testcase 1
print(my_n_choose_k(10, 1))
# Testcase 2
print(my_n_choose_k(10, 10))
# Testcase 3
print(my_n_choose_k(10, 3))
