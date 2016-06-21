'''정렬된 여러 시퀀스를 병합 후 순환'''

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

with open('c4_1.py', 'rt', encoding='utf-8') as file1, \
        open('c4_2.py', 'rt', encoding='utf-8') as file2, \
        open('somefile', 'wt', encoding='utf-8') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)
