print("키워드 인수로 선택적인 동작을 제공하자")

def remainder(number, divisor):
	return number % divisor

assert remainder(20, 7) == 6

remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# Example
def flow_rate(weight_diff, time_diff):
	return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow)	

def flow_rate(weight_diff, time_diff, period):
	return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff, 1)

# Example
def flow_rate(weight_diff, time_diff, period=1):
	return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_second = flow_rate(weight_diff, time_diff, period=3600)

# Example
def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
	return ((weight_diff / units_per_kg) / time_diff) * period

pounds_per_hour = flow_rate(weight_diff, time_diff, period=3600, units_per_kg=2.2)	

