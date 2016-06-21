'''행렬과 선형 대수 계산'''

import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)

# 전치 행렬(transpose)
print(m.T)
# 역행렬(inverse)
print(m.I)
# 벡터를 만들고 곱하기
v = np.matrix([[2], [3], [4]])
print(v)
print(m * v)

# import numpy.linalg

# Determinant
print(np.linalg.det(m))

# Eigenvalues
print(np.linalg.eigvals(m))

# mx = v에서 x풀기
x = np.linalg.solve(m, v)
print(x)
print(m * x)
print(v)
