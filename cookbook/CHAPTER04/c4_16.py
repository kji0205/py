'''무한 while 순환문을 이터레이터로 치환'''

CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(data)


import sys
f = open('etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)
    # print(n)

reader2(f)
