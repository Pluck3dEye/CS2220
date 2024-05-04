# Dung K.V. Nguyen (1607859)

import numpy as np

# Question 1
# Assign list [1, 8, 9, 15] to a variable list_a and insert 2 at index 1 using the insert method.
# Append 4 to the list_a using the append method.

print("Question 1")
list_a = [1, 8, 9, 15]
print(list_a)
list_a.insert(1, 2)
print(list_a)
list_a.append(4)
print(list_a)

# Question 2
print("\nQuestion 2")
m = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]])
# Indexing element 7
print(f"{m[1, 2]} \n")
# Indexing element 14
print(f"{m[-1, -1]} \n")
# Slicing [6, 7]
print(f"{m[1, 1:3]} \n")
# Slicing [7, 12]
print(f"{m[1:, 2]} \n")
# Slicing [[3, 4], [8, 9]]
print(f"{m[:2, 3:]} \n")

# Dung K.V. Nguyen
# Troy-IT
