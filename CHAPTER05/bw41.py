# 진정한 병렬성을 실현하려면 concurrent.futures를 고려하자
import logging
from pprint import pprint
from sys import stdout as STDOUT
from time import time

def gcd(pair):
	a, b = pair
	low = min(a, b)
	for i in range(low, 0, -1):
		if a % i == 0 and b % i == 0:
			return i

numbers = [(1963309, 2265973), (2030677, 3814172),
			(1551645, 2229620), (2039045, 2020802)]
start = time()
results = list(map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))

# 
from concurrent.futures import ThreadPoolExecutor

start = time()
pool = ThreadPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))

# 
from concurrent.futures import ProcessPoolExecutor

start = time()
pool = ProcessPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))
