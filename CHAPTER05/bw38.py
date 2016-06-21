# 스레드에서 데이터 경쟁을 막으려면 Lock을 사용하자
import logging
from pprint import pprint
from sys import stdout as STDOUT
from threading import Thread

class Counter(object):
	def __init__(self):
		self.count = 0

	def increment(self, offset):
		self.count += offset


def worker(sensor_index, how_many, counter):
	for _ in range(how_many):
		counter.increment(1)


def run_threads(func, how_many, counter):
	threads = []
	for i in range(5):
		args = (i, how_many, counter)
		thread = Thread(target=func, args=args)
		threads.append(thread)
		thread.start()
	for thread in threads:
		thread.join()


how_many = 10**5
counter = Counter()
run_threads(worker, how_many, counter)
print('Counter should be %d, found %d' % 
	(5 * how_many, counter.count))

# 
from threading import Lock

class LockingCounter(object):
	def __init__(self):
		self.lock = Lock()
		self.count = 0

	def increment(self, offset):
		with self.lock:
			self.count += offset


counter = LockingCounter()
run_threads(worker, how_many, counter)			
print('Counter should be %d, found %d' % 
	(5 * how_many, counter.count))