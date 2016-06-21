'''텍스트 데이터 읽고 쓰기'''

with open('somefile.txt', 'rt') as f:
    data = f.read()
    # print(data)

with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)
        pass

with open('somefile2.txt', 'wt') as f:
    f.write('text1')
    f.write('text2')

with open('somefile.txt', 'wt') as f:
    print('line1', file=f)
    print('line2', file=f)

with open('somefile2.txt', 'at') as f:
    f.write('text1')
    f.write('text2')


with open('u_ex150703.log', 'rt', encoding='UTF-8', newline='', errors='ignore') as f:
    for line in f:
        # print(line, end='')
        pass

with open('somefile', 'wt') as f:
    print('Hello World!', file=f)

