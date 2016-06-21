"""바이트 문자열에 텍스트 연산 수행"""

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = b'FOO:BAR,SPAM'
import re
# re.split('[:,]', data)
re.split(b'[:,]', data)


a = 'Hello World'
print(a[0])
print(a[1])
b = b'Hello World'
print(b[0])
print(b[1])
s = b
print(s)
print(s.decode('ascii'))
s = '{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
print(s)

with open('somefile.txt', 'w') as f:
    f.write('spicy')

import os
print(os.listdir('.'))
# print(os.listdir(b'.'))

