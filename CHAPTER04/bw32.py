# 지연 속성에는 __getattr__, __getattribute__, __setattr__을 사용하자
import logging

class LazyDB(object):
	def __init__(self):
		self.exists = 5

	def __getattr__(self, name):
		value = 'Value for %s' % name
		setattr(self, name, value)
		return value


data = LazyDB()
print('Before:', data.__dict__)
print('foo:   ', data.foo)
print('After:', data.__dict__)

# 
class LoggingLazyDB(LazyDB):
	def __getattr__(self, name):
		print('Called __getattr__(%s)' % name)
		return super().__getattr__(name)


data = LoggingLazyDB()
print('exists:', data.exists)
print('foo:', data.foo)
print('foo:', data.foo)

# __getattribute__
class ValidatingDB(object):
	def __init__(self):
		self.exists = 5

	def __getattribute__(self, name):
		print('Called __getattribute__(%s)' % name)
		try:
			return super().__getattribute__(name)
		except AttributeError:
			value = 'Value for %s' % name
			setattr(self, name, value)
			return value
		

data = ValidatingDB()
print('exists:', data.exists)
print('foo:', data.foo)
print('foo:', data.foo)

# 

try:
	class MissingPropertyDB(object):
		def __getattr__(self, name):
			if name == 'bad_name':
				raise AttributeError('%s is missing' % name)
			value = 'Value for %s' % name
			setattr(self, name, value)
			return value

	data = MissingPropertyDB()
	data.foo
	data.bad_name
except:
	logging.exception('Expected')
else:
	assert False


data = LoggingLazyDB()
print('Before:', data.__dict__)	
print('foo exists:', hasattr(data, 'foo'))
print('After:', data.__dict__)
print('foo exists:', hasattr(data, 'foo'))

# 
data = ValidatingDB()
print('foo exists: ', hasattr(data, 'foo'))
print('foo exists: ', hasattr(data, 'foo'))

# 
class SavingDB(object):
	def __setattr__(self, name, value):
		# Save some data to the DB log
		super().__setattr__(name, value)


# 
class LoggindSavingDB(SavingDB):
	def __setattr__(self, name, value):
		print('Called __setattr__(%s, %r)' % (name, value))
		super().__setattr__(name, value)


data = LoggindSavingDB()
print('Before: ', data.__dict__)
data.foo = 5
print('After: ', data.__dict__)
data.foo = 7
print('Finally: ', data.__dict__)

# 
class BrokenDictionaryDB(object):
	def __init__(self, data):
		self._data = {}

	def __getattribute__(self, name):
		print('Called __getattribute__(%s)' % name)
		return self._data[name]


# data = BrokenDictionaryDB({'foo': 3})
# data.foo

# 
class DictionaryDB(object):
	def __init__(self, data):
		self._data = data

	def __getattribute__(self, name):
		data_dict = super().__getattribute__('_data')
		return data_dict[name]


data = DictionaryDB({'foo': 3})
data.foo