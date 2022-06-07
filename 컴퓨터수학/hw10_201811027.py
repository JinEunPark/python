import numpy as np

A = np.zeros((3, 2))
for i in range(0, 3):
    for e in range(0, 2):
        A[i][e] = (i + 1) + (2 * (e + 1))

sum = 0
for i in range(0, 3):
    for e in range(0, 2):
        sum += A[i][e]

print("result of the sum:", sum)

A = np.array([[1, -4], [-4, 1]])
B = np.array([[2, -8], [-8, 2]])
print("A+B=", A + B)
print("A-1/2B", A - 1 / 2 * B)
print("5A", 5 * A)

A = np.array([[1, 3], [5, 7]])
invA = np.linalg.inv(A)
detA = np.linalg.det(A)
print(A)
print("invA", invA)
print("detA", detA)

A = np.array([[1, 3, 5],
              [3, 2, 1, ]])
B = np.array([[1, -4, 7],
              [-2, 5, -8],
              [3, -6, 9]])
print("dot A B", np.dot(A, B))
A = np.array([[1],
              [2],
              [3]])
B = np.array([[4, 5, 6]])
print("cross AxB:", np.cross(A.transpose(), B))
