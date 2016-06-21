class Error(Exception):
	"""Base-class for all exceptions raised by this module."""


class InvalidDensityError(Error):
	"""There was a problem with a provided density value"""


class NegativeDensityError(InvalidDensityError):
	"""A provided density value was negative."""


def determine_weight(volume, density):
	if density == 0:
		raise ValueError('Density must be positive')
	elif density < 0:
		raise NegativeDensityError