"""최적화하기 전에 프로파일하자"""

def insertion_sort(data):
	result = []
	for value in data:
		insert_value(result, value)
	return result


def insert_value(array, value):
	for i, existing in enumerate(array):
		if existing > value:
			array.insert(i, value)
			return
	array.append(value)


from random import randint

max_size = 10**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

# from cProfile import Profile
# profiler = Profile()
# profiler.runcall(test)

# import sys
# from pstats import Stats
# stats = Stats(profiler)
# stats.strip_dirs()
# stats.sort_stats('cumulative')
# stats.print_stats()

# 
from bisect import bisect_left
def insert_value(array, value):
	i = bisect_left(array, value)
	array.insert(i, value)


from cProfile import Profile
profiler = Profile()
profiler.runcall(test)

import sys
from pstats import Stats
stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
stats.print_callers()
