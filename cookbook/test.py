# print("hello")


class f(object):

    def __init__(self):
        self._num = 0

    def fib(self, n):

        if n < 2:
            print(n)
            return n
        elif n == 0:
            # print(n)
            pass
        else:
            print(n)
            # self._num += 1
            # print(self._num, " :: num")
            return f.fib(self, n - 1) + f.fib(self, n - 2)

    def __repr__(self):
        return 'num : %d' % self._num


print(f.fib(f, 3))

# print(pow(2, 10))

# a = 0
# b = 1

# for n in range(0, 30):  # n = 0 ~ 300
#     print(a, " ")

#     temp = a # a 의 현재 값을, temp 라는 변수에 임시로 담아둠
#     a = b
#     b = temp + b


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR2 = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
STATIC_ROOT2 = os.path.join(BASE_DIR, 'static')
STATIC_ROOT3 = os.path.join(os.path.dirname(__file__), 'static')
print(BASE_DIR)
print(BASE_DIR2)
print(STATIC_ROOT)
print(STATIC_ROOT2)
print(STATIC_ROOT3)
