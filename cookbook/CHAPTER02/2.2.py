"""문자열 처음이나 마지막에 텍스트 매칭"""
import os
from urllib.request import urlopen
import re


filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

#
filenames = os.listdir('.')
print(filenames)
a = [name for name in filenames if name.endswith(('.c', '.h'))]
print(a)
b = any(name.endswith('.py') for name in filenames)
print(b)

#
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# a = read_data(url)
# print(a)

choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# url.startswith(choices)
print(url.startswith(tuple(choices)))

#
print('==================')
filename = 'spam.txt'
assert filename[-4:] == '.txt'
url = 'http://www.python.org'
assert url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'

#
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))
