# 많은 함수를 동시에 실행하려면 코루틴을 고려하자

def my_coroutine():
	while True:
		received = yield
		print('Received:', received)


it = my_coroutine()
next(it)
it.send('First')		
it.send('Second')

# 
def minimize():
	current = yield
	while True:
		value = yield current
		current = min(value, current)


it = minimize()
next(it)
print(it.send(10))		
print(it.send(4))		
print(it.send(22))		
print(it.send(-1))		
