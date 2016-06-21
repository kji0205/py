# copyreg로 pickle을 신뢰할 수 있게 만들자
import logging
from pprint import pprint
from sys import stdout as STDOUT

class GameState(object):
	def __init__(self):
		self.level = 0
		self.lives = 4

state = GameState()
state.level += 1
state.lives -= 1

# 
import pickle

state_path = 'game_state.bin'		
with open(state_path, 'wb') as f:
	pickle.dump(state, f)

with open(state_path, 'rb')	as f:
	state_after = pickle.load(f)
print(state_after.__dict__)

# 
class GameState(object):
	def __init__(self):
		self.level = 0
		self.lives = 4
		self.points = 0


state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

# 
with open(state_path, 'rb') as f:
	state_after = pickle.load(f)
print(state_after.__dict__)

assert isinstance(state_after, GameState)

# 
class GameState(object):
	def __init__(self, level=0, lives=4, points=0):
		self.level = level
		self.lives = lives
		self.points = points


def pickle_game_state(game_state):
	kwargs = game_state.__dict__
	return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
	return GameState(**kwargs)


import copyreg
copyreg.pickle(GameState, pickle_game_state)	

state = GameState()
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

# 
class GameState(object):
	def __init__(self, level=0, lives=4, points=0, magic=5):
		self.level = level
		self.points = points
		self.magic = magic


state_after = pickle.loads(serialized)
print(state_after.__dict__)

# 
class GameState(object):
	def __init__(self, level=0, points=0, magic=5):
		self.level = level
		self.points = points
		self.magic = magic


try:
	pass
	# pickle.loads(serialized)
except:
	logging.exception('Expected')
else:
	pass
	# assert False

# 
def pickle_game_state(game_from datetime import datetime, timezone

now = datetime(2014, 8, 10, 18, 18, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)tate):
	kwargs = game_state.__dict__
	kwargs['version'] = 2
	return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
	version = kwargs.pop('version', 1)
	if version == 1:
		kwargs.pop('lives')
	return GameState(**kwargs)


copyreg.pickle(GameState, pickle_game_state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)


# 
copyreg.dispatch_table.clear()
state = GameState()
serialized = pickle.dumps(state)
del GameState

class BetterGameState(object):
	def __init__(self, level=0, points=0, magic=5):
		self.level = level
		self.points = points
		self.magic = magic



print(serialized[:25])

copyreg.pickle(BetterGameState, pickle_game_state)

state = BetterGameState()
serialized = pickle.dumps(state)
print(serialized[:35])