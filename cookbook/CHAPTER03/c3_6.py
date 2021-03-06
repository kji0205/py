'''복소수 계산'''

a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)
print(a.real)
print(a.imag)
print(a.conjugate())

print(a + b)
print(a * b)
print(a / b)
print(abs(a))

# print('a {0}'.format(a))

import cmath

print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

import numpy as np

a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
print(a)
print(a + 2)
print(np.sin(a))

import math
# print(math.sqrt(-1))
print(cmath.sqrt(-1))
