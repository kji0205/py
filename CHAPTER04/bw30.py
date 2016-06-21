# 속성을 리팩토링하는 대신 @property를 고려하자
import logging
from pprint import pprint
from sys import stdout as STDOUT

from datetime import datetime, timedelta

class Bucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.quota = 0

	def __repr__(self):
		return 'Bucket(quota=%d)' % self.quota


def fill(bucket, amount):
	now = datetime.now()
	print('now:', now)
	print('bucket.reset_time:', bucket.reset_time)
	print('bucket.period_delta:', bucket.period_delta)
	if now - bucket.reset_time > bucket.period_delta:
		bucket.quota = 0
		bucket.reset_time = now
	bucket.quota += amount


def deduct(bucket, amount):
	now = datetime.now()
	if now - bucket.reset_time > bucket.period_delta:
		return False
	if bucket.quota - amount < 0:
		return False
	bucket.quota -= amount
	return True


bucket = Bucket(60)
fill(bucket, 100)
print(bucket)

if deduct(bucket, 99):
	print('Had 99 quota')
else:
	print('Not enough for 99 quota')
print(bucket)

if deduct(bucket, 3):
	print('Had 3 quota')
else:
	print('Not enough for 3 quota')
print(bucket)

# 
class Bucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.max_quota = 0
		self.quota_consumed = 0

	def __repr__(self):
		return ('Bucket(max_quota=%d, quota_consumed=%d)' %
			(self.max_quota, self.quota_consumed))

	@property
	def quota(self):
	    return self.max_quota - self.quota_consumed

	@quota.setter
	def quota(self, amount):
		delta = self.max_quota - amount
		if amount == 0:
			# 새 기간의 할당량을 리셋함
			self.quota_consumed = 0
			self.max_quota = 0
		elif delta < 0:
			# 새 기간의 할당량을 채움
			assert self.quota_consumed == 0
			self.max_quota = amount
		else:
			# 기간 동안 할당량을 소비함
			assert self.max_quota >= self.quota_consumed
			self.quota_consumed += delta


bucket = Bucket(60)
print('Initial', bucket)
fill(bucket, 100)
print('Filled', bucket)

if deduct(bucket, 99):
	print('Had 99 quota')
else:
	print('Not enough for 99 quota')

print('Now', bucket)	

if deduct(bucket, 3):
	print('Had 3 quota')
else:
	print('Not enough for 3 quota')

print('Still', bucket)