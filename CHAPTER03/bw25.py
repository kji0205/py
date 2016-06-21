# super로 부모 클래스를 초기화하자
import logging
from pprint import pprint
from sys import stdout as STDOUT

class MyBaseClass(object):
	def __init__(self, value):
		self.value = value


class MyChildClass(MyBaseClass):
	def __init__(self):
		MyBaseClass.__init__(self, 5)


# Example
class TimesTwo(object):
	def __init__(self):
		self.value *= 2


class PlusFive(object):
	def __init__(self):
		self.value += 5


# Example
class OneWay(MyBaseClass, TimesTwo, PlusFive):
	def __init__(self, value):
		MyBaseClass.__init__(self, value)
		TimesTwo.__init__(self)
		PlusFive.__init__(self)


foo = OneWay(5)
print('First ordering is (5 * 2) + 5 =', foo.value)

class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
	def __init__(self, value):
		MyBaseClass.__init__(self, value)
		TimesTwo.__init__(self)
		PlusFive.__init__(self)


bar = AnotherWay(5)
print('Second ordering still is', bar.value)

# Example
class TimesFive(MyBaseClass):
	def __init__(self, value):
		MyBaseClass.__init__(self, value)
		self.value *= 5


class PlusTwo(MyBaseClass):
	def __init__(self, value):
		MyBaseClass.__init__(self, value)
		self.value += 2


class ThisWay(TimesFive, PlusTwo):
	def __init__(self, value):
		TimesFive.__init__(self, value)
		PlusTwo.__init__(self, value)


foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27 but is', foo.value)


# Example - Python2
class TimesFiveCorrect(MyBaseClass):
	def __init__(self, value):
		super(TimesFiveCorrect, self).__init__(value)
		self.value *= 5


class PlusTwoCorrect(MyBaseClass):
	def __init__(self, value):
		super(PlusTwoCorrect, self).__init__(value)
		self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
	def __init__(self, value):
		super(GoodWay, self).__init__(value)


foo = GoodWay(5)
print ('Should be 5 * (5 + 2) = 35 and is', foo.value)
pprint(GoodWay.mro())


# Example - python3
class Explicit(MyBaseClass):
	def __init__(self, value):
		super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
	def __init__(self, value):
		super().__init__(value * 2)


assert Explicit(10).value == Implicit(10).value