import logging
from pprint import pprint
from sys import stdout as STDOUT

from time import sleep
from datetime import datetime

print("동적 기본 인수를 지정하려면 None과 docstring을 사용하자")

def log(message, when=datetime.now()):
	print('%s: %s' % (when, message))

log('Hi there!')	
sleep(0.1)
log('Hi again!')

def log(message, when=None):
	"""Log a message with a timestamp.

	Args:
		message: Message to print.
		when: datetime of when the message occurred.
			Defaults to the present time.
	"""
	when = datetime.now() if when is None else when
	print('%s: %s' % (when, message))

log('Hi there!')
sleep(0.1)
log('Hi again!')

# Example
import json 

def decode(data, default={}):
	try:
		return json.loads(data)
	except ValueError:
		return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['beep'] = 1
print('Foo:', foo)
print('Bar:', bar)

assert foo is bar

def decode(data, default=None):
	"""Load JSON data from a string.

	Args:
		data: JSON data to decode.
		default: Value to return if decoding fails.
			Defaults to an empty dictionary.
	"""
	if default is None:
		default = {}
	try:
		return json.loads(data)
	except ValueError:
		return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

