'''2진수, 8진수, 16진수 작업'''

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

x = -1234
print(format(x, 'b'))
print(format(x, 'x'))

x = -1234
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))

print(int('4d2', 16))

import os

# os.chmod('script.py', 0755)
os.chmod('script.py', 0o0755)

# print(os.listdir('.'))
