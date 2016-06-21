import logging
from pprint import pprint
from sys import stdout as STDOUT

from collections import deque
from random import randint

a = {}
a['foo'] = 1
a['bar'] = 2

while True:
	z = randint(99, 1013)
	b = {}
	for i in range(z):
		b[i] = i
	b['foo'] = 1
	b['foo'] = 2
	for i in range(z):
		del b[i]
	if str(b) != str(a):
		break

print(a)
print(b)
print('Equal?', a == b)

from collections import OrderedDict

a = OrderedDict()
a['foo'] = 1
a['bar'] = 2

b = OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'

for value1, value2 in zip(a.values(), b.values()):
	print(value1, value2)

# 
stats = {}
key = 'my_counter'
if key not in stats:
	stats[key] = 0
stats[key] += 1

from collections import defaultdict
stats = defaultdict(int)
stats['my_counter'] += 1
print(dict(stats))

# 
from heapq import *
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)

print(heappop(a), heappop(a), heappop(a), heappop(a))

a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
assert a[0] == nsmallest(1, a)[0] == 3

print('Before:', a)
a.sort()
print('After: ', a)

# 
x = list(range(10**6))
i = x.index(991234)
print(i)

#
from bisect import bisect_left
i = bisect_left(x, 991234)
print(i)

# 
from timeit import timeit
print(timeit(
	'a.index(len(a)-1)',
	'a = list(range(100))',
	number=1000))
print(timeit(
	'bisect_left(a, len(a)-1)',
	'from bisect import bisect_left;'
	'a = list(range(10**6))',
	number=1000))