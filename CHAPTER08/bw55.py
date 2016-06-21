"""디버깅 출력용으로는 repr 문자렬을 사용하자"""

a = '\x07'
print(repr(a))

b = eval(repr(a))
assert a == b

print(repr(5))
print(repr('5'))

print('%r' % 5)
print('%r' % '5')

# 
class OpaqueClass(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# def __repr__(self):
	# 	return 'BetterClass(%d, %d)' % (self.x, self.y)


obj = OpaqueClass(1, 2)
print(obj)

obj = OpaqueClass(1, 2)
print(obj.__dict__)
