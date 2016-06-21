from unittest import TestCase, main
from bw56 import to_str

class UtilTestCase(TestCase):
	"""docstring for UtilTestCase"""
	def test_to_str_bytes(self):
		self.assertEqual('hello', to_str(b'hello'))

	def test_to_str_str(self):
		self.assertEqual('hello', to_str('hello'))

	def test_to_str_bad(self):
		self.assertRaises(TypeError, to_str, object())


if __name__ == '__main__':
	main()