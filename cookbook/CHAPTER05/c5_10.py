import os
import mmap


def memory_map(filename, access=mmap.ACCESS_COPY):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 1000000
with open('data', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
print(m[0:10])
print(m[0])

# 슬라이스 재할당
m[0:11] = b'Hello World'
m.close()

# 수정 검증
with open('data', 'rb') as f:
    print(f.read(11))

with memory_map('data') as m:
    print(len(m))
    print(m[0:10])

m.closed

m = memory_map('data')
# 부호없는 정수형(unsigend integer)의 메모리뷰
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])

m[0:4] = b'\x07\x01\x00\x00'
print(v[0])

