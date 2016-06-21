'''바이너리 데이터 읽고 쓰기'''

# 파일 전체를 하나의 바이트 문자열로 읽기
with open('somefile.bin', 'rb') as f:
    data = f.read()
# 바이너리 데이터 파일에 쓰기
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')

t = 'Hello World'
print(t[0])
for c in t:
    print(c, end='')

print()
b = b'Hello World'
print(b[0])
for c in b:
    print(c, end='\n')

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

print(text)

with open('somefile.bin', 'wb') as f:
    text = 'Hello World2'
    f.write(text.encode('utf-8'))

import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)
print(a)
