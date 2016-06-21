def log(message, values):
	if not values:
		print(message)
	else:
		values_str = ', '.join(str(x) for x in values)
		print('%s: %s' % (message, values_str))

log('My numbers are', [1, 2])		
log('Hi there', [])


# Example
def log(message, *values):
	if not values:
		print(message)
	else:
		values_str = ', '.join(str(x) for x in values)
		print('%s: %s' % (message, values_str))

log('My numbers are', 1, 2)
log('Hi there')			

fovarites = [7, 33, 99]
log('fovarite colors', *fovarites)

# Example
def my_generator():
	for i in range(10):
		yield i

def my_func(*args):
	print(args)

it = my_generator()
my_func(*it)

# Example
def log(sequence, message, *values):
	if not values:
		print('%s: %s' % (sequence, message))
	else:
		values_str = ', '.join(str(x) for x in values)
		print('%s: %s: %s' % (sequence, message, values_str))

log(1, 'fovarites', 7, 33)
log('fovarite numbers', 7, 33)
