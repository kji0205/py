import logging
from pprint import pprint
from sys import stdout as STDOUT

print("인수를 순회할 때는 방어적으로 하자")

def normalize(numbers):
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100 * value / total
		result.append(percent)
	return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)


def read_visits(data_path):
	with open(data_path) as f:
		for line in f:
			yield int(line)

it = read_visits('my_numbers.txt')			
percentages = normalize(it)
print(percentages)

it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))

# Example
def normalize_copy(numbers):
	numbers = list(numbers)		# copy to iterator
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100 * value / total
		result.append(percent)
	return result

it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)

# Example
def normalize_func(get_iter):
	total = sum(get_iter())
	result = []
	for value in get_iter():
		percent = 100 * value / total
		result.append(percent)
	return result

path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))

# Example
class ReadVisits(object):
	def __init__(self, data_path):
		self.data_path = data_path

	def __iter__(self):
		with open(self.data_path) as f:
			for line in f:
				yield int(line)


visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)

# Example
def normalize_defensive(numbers):
	if iter(numbers) is iter(numbers):
		raise TypeError('Must supply a container')
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100 * value / total
		result.append(percent)
	return result

visits = [15, 35, 80]
normalize_defensive(visits)
visits = ReadVisits(path)
normalize_defensive(visits)

# Example
it = iter(visits)
normalize_defensive(it)
