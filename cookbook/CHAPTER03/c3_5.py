'''바이트에서 큰 숫자를 패킹/언패킹'''

data = b'\x00\x123V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
data1 = b'\xef'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data1, 'little'))
print(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

print(data)

import struct
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)

x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

x = 523 ** 23
print(x)
# print(x.to_bytes(16, 'little'))
print(x.bit_length())
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))
