import logging
from pprint import pprint
from sys import stdout as STDOUT

ALIVE = '*'
EMPTY = '-'

from collections import namedtuple
Query = namedtuple('Query', ('y', 'x'))

def count_neighbors(y, x):
	n_ = yield Query(y + 1, x + 0)
	ne = yield Query(y + 1, x + 1)
	e_ = yield Query(y + 0, x + 1)
	se = yield Query(y - 1, x + 1)
	s_ = yield Query(y - 1, x + 0)
	sw = yield Query(y + 0, x - 1)
	w_ = yield Query(y + 0, x - 1)
	nw = yield Query(y + 0, x - 1)
	neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
	count = 0
	for state in neighbor_states:
		if state == ALIVE:
			count += 1
	return count


it = count_neighbors(10, 5)	
q1 = next(it)
print('First yield: ', q1)
q2 = it.send(ALIVE)
print('Second yield:', q2)
q3 = it.send(ALIVE)
print('...')
q4 = it.send(EMPTY)
q5 = it.send(EMPTY)
q6 = it.send(EMPTY)
q7 = it.send(EMPTY)
q8 = it.send(EMPTY)
try:
	it.send(EMPTY)
except StopIteration as e:
	print('Count: ', e.value)

# 
Transition = namedtuple('Transition', ('y', 'x', 'state'))

# 
def game_logic(state, neighbors):
	pass

def step_cell(y, x):
	state = yield Query(y, x)
	neighbors = yield from count_neighbors(y, x)
	next_state = game_logic(state, neighbors)
	yield Transition(y, x, next_state)

# 
def game_logic(state, neighbors):
	if state == ALIVE:
		if neighbors < 2:
			return EMPTY
		elif neighbors > 3:
			return EMPTY
	else:
		if neighbors == 3:
			return ALIVE
	return state


# 
it = step_cell(10, 5)
q0 = next(it)	# Initial loation query
print('Me: ', q0)
q1 = it.send(ALIVE)	# Send my status, get neighbor query
print('Q1: ', q1)
print('...')
q2 = it.send(ALIVE)
q3 = it.send(ALIVE)
q4 = it.send(ALIVE)
q5 = it.send(ALIVE)
q6 = it.send(ALIVE)
q7 = it.send(ALIVE)
q8 = it.send(ALIVE)
t1 = it.send(ALIVE)		# Send for q8, get game decision
print('Outcome: ', t1)


# 
TICK = object()

def simulate(height, width):
	while True:
		for y in range(height):
			for x in range(width):
				yield from step_cell(y, x)
		yield TICK


# 
class Grid(object):
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.rows = []
		for _ in range(self.height):
			self.rows.append([EMPTY] * self.width)
	
	def __str__(self):
		output = ''
		for row in self.rows:
			for cell in row:
				output += cell
			output += '\n'
		return output

	def query(self, y, x):
		return self.rows[y % self.height][x % self.width]

	def assign(self, y, x, state):
		self.rows[y % self.height][x % self.width] = state

# 
def live_a_generation(grid, sim):
	progeny = Grid(grid.height, grid.width)
	item = next(sim)
	while item is not TICK:
		if isinstance(item, Query):
			state = grid.query(item.y, item.x)
			item = sim.send(state)
		else:	# Must be a Transition
			progeny.assign(item.y, item.x, item.state)
			item = next(sim)
	return progeny

# 
grid = Grid(5, 9)
grid.assign(0, 3, ALIVE)
grid.assign(1, 4, ALIVE)
grid.assign(2, 2, ALIVE)
grid.assign(2, 3, ALIVE)
grid.assign(2, 4, ALIVE)
print(grid)

# 
class ColumnPrinter(object):
	def __init__(self):
		self.columns = []

	def append(self, data):
		self.columns.append(data)

	def __str__(self):
		row_count = 1
		for data in self.columns:
			row_count = max(row_count, len(data.splitlines()) + 1)
		rows = [''] * row_count
		for j in range(row_count):
			for i, data in enumerate(self.columns):
				line = data.splitlines()[max(0, j - 1)]
				if j == 0:
					padding = ' ' * (len(line) // 2)
					rows[j] += padding + str(i) + padding
				else:
					rows[j] += line
				if (i + 1) < len(self.columns):
					rows[j] += ' | '
		return '\n'.join(rows)

columns = ColumnPrinter()
sim = simulate(grid.height, grid.width)
for i in range(5):
	columns.append(str(grid))
	grid = live_a_generation(grid, sim)

print(columns)

# 
grid = Grid(5, 5)
grid.assign(1, 1, ALIVE)
grid.assign(2, 2, ALIVE)
grid.assign(2, 3, ALIVE)
grid.assign(3, 3, ALIVE)

columns = ColumnPrinter()
sim = simulate(grid.height, grid.width)
for i in range(5):
	columns.append(str(grid))
	grid = live_a_generation(grid, sim)

print(columns)
a = input('End...')