"""여러 매핑을 단일 매핑으로 합치기"""
from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))

#
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y']

#
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print('values: %s' % values)

#
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
print(values)

#
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

#
a['x'] = 13
print("merged['x']:", merged['x'])

merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x'])
