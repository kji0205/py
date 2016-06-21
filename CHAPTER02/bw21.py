# 키워드 전용 인수로 명료성을 강요하자

def safe_division(number, division, ignore_overflow, ignore_zero_division):
	try:
		return number / division
	except OverflowError:
		if ignore_overflow:
			return 0
		else:
			raise
	except ZeroDivisionError:
		if ignore_zero_division:
			return float('inf')
		else:
			raise

def safe_division_c(number, division, *, ignore_overflow, ignore_zero_division):
	try:
		return number / division
	except OverflowError:
		if ignore_overflow:
			return 0
		else:
			raise
	except ZeroDivisionError:
		if ignore_zero_division:
			return float('inf')
		else:
			raise


result = safe_division(1, 10**500, True, False)			
print(result)

result = safe_division(1, 0, False, True)
print(result)

# result = safe_division_c(1, 10**500, True, False)

result = safe_division_c(1, 0, ignore_zero_division=True)
print(result)