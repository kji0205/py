# 메타클래스로 서브클래스를 검증하자
import logging
from pprint import pprint
from sys import stdout as STDOUT

class Meta(type):
	def __new__(meta, name, bases, class_dict):
		print((meta, name, bases, class_dict))
		return type.__new__(meta, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
	stuff = 123

	def foo(self):
		pass


# 
class ValidatePolygon(type):
	def __new__(meta, name, bases, class_dict):
		# 추상 Polygon 클래스는 검증하지 않음
		if bases != (object,):
			if class_dict['sides'] < 3:
				raise ValueError('Polygons need 3+ sides')
		return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
	sides = None	# 서브클래스에서 설정함

	@classmethod
	def interior_angels(cls):
		return (cls.sides - 2) * 180


class Triangle(Polygon):
	sides = 3


print('Before class')
class Line(Polygon):
	print('Before sides')
	sides = 1
	print('After sides')
print('After class')