"""딕셔너리의 키를 여러 값에 매핑하기"""
from collections import defaultdict


a = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
print(a)
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}
print(e)

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)

d = {}
pairs = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print('test', d)
