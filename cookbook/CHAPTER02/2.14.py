"""문자열 합치기"""

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
a = ' '.join(parts)
print(a)
a = ','.join(parts)
print(a)
a = ''.join(parts)
print(a)
#
a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
#
print('{} {}'.format(a, b))
print(a + ' ' + b)
a = 'Hello' 'World'
print(a)
#
s = ''
for p in parts:
    s += p
#
data = ['ACME', 50, 91.1]
d = ','.join(str(d) for d in data)
print(d)
#
print(a, b, sep=':')

with open('somefile.txt', 'w') as f:
    f.write(a + b)
#


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ''.join(sample())
print(text)

with open('somefile.txt', 'w') as f:
    for part in sample():
        f.write(part)


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    with open('somefile.txt', 'w') as f:
        f.write('part')
