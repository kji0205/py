# 파이썬2의 키워드 전용 인수

def print_args(*args, **kwargs):
	print('Positional', args)
	print('Keyword:', kwargs)

print_args(1, 2, foo='bar', stuff='meep')	

def safe_division_d(number, divisor, **kwargs):
	ignore_overflow = kwargs.pop('ignore_overflow', False)
	ignore_zero_div = kwargs.pop('ignore_zero_division', False)
	if kwargs:
		raise TypeError('Unexpected **kwargs: %r' % kwargs)

safe_division_d(1, 10)
safe_division_d(1, 0, ignore_zero_division=True)
safe_division_d(1, 10**500, ignore_overflow=True)

safe_division_d(1, 0, False, True)
