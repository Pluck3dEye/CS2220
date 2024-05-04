# Dung K.V. Nguyen (1607859)

import numpy as np

# Problem #1 page 188

print("\nProblem 1")
students = [
    {"name": "Student_A", "id": 12345, "grade": "A"},
    {"name": "Student_B", "id": 54321, "grade": "B"},
    {"name": "Student_C", "id": 12332, "grade": "C"},
    {"name": "Student_D", "id": 34554, "grade": "D"}
]

with open("student.txt", "w") as file:
    for student in students:
        file.write(f"{student["name"]}, {student["id"]}, {student["grade"]}\n")

with open("student.txt", "r") as file:
    for line in file:
        name_, id_, grade_ = line.strip().split(", ")
        print(f"Name: {name_}, ID: {id_}, Grade: {grade_}")

# Problem #3 page 188

print("\nProblem 3")
random_array = np.random.randint(1, 7, size=(8, 8))
np.savetxt('data.csv', random_array, delimiter=',', fmt="%d")

my_csv = np.loadtxt('data.csv', delimiter=',')
print(my_csv)
