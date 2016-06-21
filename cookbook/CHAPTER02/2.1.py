"""여러 구분자로 문자열 나누기"""
import re


line = 'asdf fjdk; afed, fjek,asdf,       foo'
s = re.split(r'[;,\s]\s*', line)
print(s)

#
fileds = re.split(r'(;|,|\s)\s*', line)
print(fileds)

#
values = fileds[::2]
delimiters = fileds[1::2] + ['']
print(values)
print(delimiters)

#
s = re.split(r'(?:,|;|\s*)', line)
print(s)
