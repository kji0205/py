"""문자열에 변수 사용"""
import sys
import string

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))
#
name = 'Guido'
n = 37
print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
print(s.format_map(vars(a)))


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('Your favorite color is  {color}'))

name = 'Guido'
n = 37
# s = '%{name} has %{n} messages.' % vars()

s = string.Template('$name has $n messages.')
print(s.substitute(vars()))
