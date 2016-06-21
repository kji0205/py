"""루트 Exception을 정의해서 API로부터 호출자를 보호하자"""
import logging
import my_module


try:
	weight = my_module.determine_weight(1, -1)
except my_module.NegativeDensityError as e:
	raise ValueError('Must supply non-negative density') from e
except my_module.InvalidDensityError:
	weight = 0
except my_module.Error as e:
	logging.error('Bug in the calling code: %s', e)
except Exception as e:
	logging.error('Bug in the API code: %s', e)	
	raise