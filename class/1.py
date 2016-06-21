class Service:
	secret = "youngu have two things"
	def __init__(self, name):
		self.name = name

	def sum(self, a, b):
		result = a + b
		print("%s %s + %s = %s" % (self.name, a, b, result))

pay = Service("Jimmy")
# pay.setname("Jimmy")
pay.sum(1, 1)
