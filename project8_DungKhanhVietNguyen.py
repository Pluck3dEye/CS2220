# Dung K.V. Nguyen (1607859)

# Problem #1 page 153

def my_bin_2_dec(list_):
    decimal = 0
    power_2 = 1
    length_of_bin = len(list_)
    decimal += list_[length_of_bin - 1] * power_2

    for i in range(length_of_bin - 2, -1, -1):
        power_2 *= 2
        decimal += list_[i] * power_2

    return decimal


# Testcase
print(my_bin_2_dec([1, 1, 1]))

print(my_bin_2_dec([1, 0, 1, 0, 1, 0, 1]))

print(my_bin_2_dec([1] * 25))

print(my_bin_2_dec([0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0]))
# 0001 0111 0010 --> 370

print(my_bin_2_dec([1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]))
# 110 1111 0101 1011 1011 --> 456123


# Problem 2 with n base

# def my_dec_2_n_base(input_, n):
#     divisor = 1
#     str_binary = ""
#     while divisor != 0:
#         divisor = (input_ // n)
#         remainder = input_ % n
#         if remainder >= 10:
#             str_binary += chr(remainder + 55)
#         else:
#             str_binary += str(remainder)
#         input_ = divisor
#
#     str_binary = str_binary[::-1]
#     return str_binary
#
#
# print(my_dec_2_n_base(1607859, 16))
# binary_1 = [int(d) for d in list(my_dec_2_n_base(12654, 2))] # Problem 3
# print(binary_1)
# d = my_bin_2_dec(binary_1)
# print(d)

# Problem 4

# def my_bin_adder(b1, b2):
#     carry = 0
#     result = []
#     max_len = max(len(b1), len(b2))
#
#     if max_len > len(b1):  # Add 0 to smaller number
#         for i in range(max_len - len(b1)):
#             b1.insert(0, 0)
#     else:
#         for i in range(max_len - len(b2)):
#             b2.insert(0, 0)
#
#     for i in range(max_len - 1, -1, -1):
#         p = carry  # result of same column of digits in addition from the right
#         p += 1 if b1[i] == 1 else 0
#         p += 1 if b2[i] == 1 else 0
#         result.insert(0, 1 if p % 2 == 1 else 0)  # p = {0, 2} --> 0 | # p = {1,3} --> 1
#         carry = 0 if p < 2 else 1  # p = {2, 3} --> carry = 1
#
#     if carry != 0:  # if carry still exist after last col addition from the right
#         result.insert(0, 1)
#     return result
#
#
# print(my_bin_adder([1, 1, 1, 1, 1], [1]))
# print(my_bin_adder([1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0]))
# print(my_bin_adder([1, 1, 0], [1, 0, 1]))
