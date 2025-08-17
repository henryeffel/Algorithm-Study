import numpy as np

A = np.array([[1, 2, 3],
              [2, 3, 5],
              [1, 0, 2]], dtype=float)

if np.linalg.det(A) != 0:
    A_inv = np.linalg.inv(A)
    print(A_inv)
else:
    print("역행렬이 존재하지 않습니다.")
