'''문자열을 시간으로 변환'''

from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

print(z)
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)


def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

print(parse_ymd('2016-04-20'))
