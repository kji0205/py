# 객체를 범용으로 생성하려면 @classmethod 다형성을 이용하자
import logging
from pprint import pprint
from sys import stdout as STDOUT
import os

class InputData(object):
	def read(self):
		raise NotImplementError


class PathInputData(InputData):
	def __init__(self, path):
		super().__init__()
		self.path = path

	def read(self):
		return open(self.path).read()


class Worker(object):
	def __init__(self, input_data):
		self.input_data = input_data
		self.result = None

	def map(self):
		raise NotImplementError

	def reduce(self, other):
		raise NotImplementError


class LineCountWorker(Worker):
	def map(self):
		data = self.input_data.read()
		self.result = data.count('\n')

	def reduce(self, other):
		self.result += other.result


# Example
def generate_inputs(data_dir):
	for name in os.listdir(data_dir):
		yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
	workers = []
	for input_data in input_list:
		workers.append(LineCountWorker(input_data))		
	return workers


from threading import Thread

def execute(workers):
	threads = [Thread(target=w.map) for w in workers]
	for thread in threads: 
		thread.start()
	for thread in threads: 
		thread.join()

	first, rest = workers[0], workers[1:]
	for worker in rest:
		first.reduce(worker)
	return first.result


def mapreduce(data_dir):
	inputs = generate_inputs(data_dir)
	workers = create_workers(inputs)
	# print('inputs:', inputs)
	# print('workers:', workers)
	return execute(workers)


from tempfile import TemporaryDirectory
import random

def write_test_files(tmpdir):
	for i in range(100):
		with open(os.path.join(tmpdir, str(i)), 'w') as f:
			f.write('\n' * random.randint(0, 100))



with TemporaryDirectory() as tmpdir:
	write_test_files(tmpdir)
	# print(tmpdir)
	result = mapreduce(tmpdir)


print('There are', result, 'lines')


# Example
class GenericInputData(object):
	def read(self):
		raise NotImplementError

	@classmethod
	def generate_inputs(cls, config):
		raise NotImplementError


class PathInputData(GenericInputData):
	def __init__(self, path):
		super().__init__()
		self.path = path

	def read(self):
		return open(self.path).read()

	@classmethod
	def generate_inputs(cls, config):
		data_dir = config['data_dir']
		for name in os.listdir(data_dir):
			yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
	def __init__(self, input_data):
		self.input_data = input_data
		self.result = None

	def map(self):
		raise NotImplementError

	def reduce(self, other):
		raise NotImplementError

	@classmethod
	def create_workers(cls, input_class, config):
		workers = []
		for input_data in input_class.generate_inputs(config):
			workers.append(cls(input_data))
		return workers


class LineCountWorker(GenericWorker):
	def map(self):
		data = self.input_data.read()
		self.result = data.count('\n')

	def reduce(self, other):
		self.result += other.result


def mapreduce(worker_class, input_class, config):
	workers = worker_class.create_workers(input_class, config)
	return execute(workers)


with TemporaryDirectory() as tmpdir:
	write_test_files(tmpdir)
	config = {'data_dir': tmpdir}	
	result = mapreduce(LineCountWorker, PathInputData, config)

print('There are', result, 'lines')