import numpy as np

A = np.array([[1499 / 852, -116 / 213, 5 / 142],
              [-116 / 213, 287 / 852, -3 / 71],
              [5 / 142, -3 / 71, 1 / 142]])
B = np.array([[1, 1, 1, 1],
              [2, 3, 5, 6],
              [4, 9, 25, 36]])
result = np.dot(A, B)
Y = np.array([[1],
              [0],
              [1],
              [2]])
result2 = np.dot(result, Y)
print(result2)
