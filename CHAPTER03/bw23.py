# 인터페이스가 간단하면 클래스 대신 함수를 받자
import logging
from pprint import pprint
from sys import stdout as STDOUT

names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)

# Example
from collections import defaultdict

def log_missing():
	print('Key added')
	return 0

current = {'green': 12, 'blue': 3}	
increments = [
	('red', 5),
	('blue', 17),
	('orange', 9),
]
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
	result[key] += amount
print('After: ', dict(result))	


# Example
def increments_with_report(current, increments):
	added_count = 0

	def missing():
		nonlocal added_count	# 상태 보존 클로저
		added_count += 1
		return 0

	result = defaultdict(missing, current)
	for key, amount in increments:
		result[key] += amount

	return result, added_count

result, count = increments_with_report(current, increments)	
assert count == 2


class CountMissing(object):
	def __init__(self):
		self.added = 0

	def missing(self):
		self.added += 1
		return 0


counter = CountMissing()
result = defaultdict(counter.missing, current)

for key, amount in increments:
	result[key] += amount
assert counter.added == 2

# Example
class BetterCountMissing(object):
	def __init__(self):
		self.added = 0

	def __call__(self):
		self.added += 1
		return 0

counter = BetterCountMissing()
counter()
assert callable(counter)

counter = BetterCountMissing()
result = defaultdict(counter, current)	# __call__이 필요함
for key, amount in increments:
	result[key] += amount
assert counter.added == 2
