"""텍스트 검색과 치환"""
import re
from calendar import month_abbr

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

#
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
a = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(a)

#
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
a = datepat.sub(r'\3-\1-\2', text)
print(a)


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))

newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
