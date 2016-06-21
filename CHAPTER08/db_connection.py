import sys

class TestingDatabase(object):
	pass


class RealDatabase(object):
	pass


class Win32Database(object):
	pass


class PosixDatabase(object):
	pass
				

# if __main__.TESTING:
# 	Database = TestingDatabase
# else:
# 	Database = RealDatabase

if sys.platform.startswith('wind32'):
	Database = Win32Database
else:
	Database = PosixDatabase