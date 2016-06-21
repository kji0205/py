"""문자열에서 문자 잘라내기"""
import re

s = '    hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

#
s = ' hello    world       \n'
s = s.strip()
print(s)

print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))

#
print('====')
with open('somefile1.txt', 'rt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
