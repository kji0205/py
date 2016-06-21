# 재사용 가능한 try/finally 동작을 만들려면 contextlib와 with문을 고려하자
import logging
from pprint import pprint
from sys import stdout as STDOUT

from threading import Lock

lock = Lock()
with lock:
	print('Lock is held')

lock.acquire()
try:
	print('Lock is held')
finally:
	lock.release()

# 
def my_function():
	logging.debug('Some debug data')
	logging.error('Error log here')
	logging.debug('More debug data')

my_function()

# 
from contextlib import contextmanager

@contextmanager
def debug_logging(level):
	logger = logging.getLogger()
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield
	finally:
		logger.setLevel(old_level)

with debug_logging(logging.DEBUG):
	print('Inside:')	
	my_function()
print('After:')
my_function()

# 
@contextmanager
def log_level(level, name):
	logger = logging.getLogger(name)
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield logger
	finally:
		logger.setLevel(old_level)

with log_level(logging.DEBUG, 'my-log')	as logger:
	logger.debug('This is my message!')
	logging.debug('This will not print')

logger = logging.getLogger('my-log')	
logger.debug('Debug will not print')
logger.error('Error will print')
