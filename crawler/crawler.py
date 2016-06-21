import os
import requests
import bs4

def to_str(byte_or_str):
    if isinstance(byte_or_str, bytes):
        value = byte_or_str.decode('utf-8')
    else:
        value = byte_or_str
    return value  # str 인스턴스


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # bytes 인스턴스


with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))

print(to_bytes('test'))