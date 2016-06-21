'''시간대 관련 날짜 처리'''

from datetime import datetime, timedelta
from pytz import timezone

# d = datetime(2012, 12, 21, 9, 30, 0)
d = datetime.today()
print(d)

# 시카고에 맞게 현지화
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# 방갈로르 시간으로 변환
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

d = datetime.today()
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)

later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

import pytz
print('loc_d {}'.format(loc_d))
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)

later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

print(pytz.country_timezones)
