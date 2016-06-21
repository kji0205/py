import gc
found_objects = gc.get_objects()
print('%d objects before' % len(found_objects))

# import waste_memory
# x = waste_memory.run()
# found_objects = gc.get_objects()

# print('%d objects after' % len(found_objects))
# for obj in found_objects[:3]:
# 	print(repr(obj)[:100])

import tracemalloc
tracemalloc.start(10)

time1 = tracemalloc.take_snapshot()
# import waste_memory
# x = waste_memory.run()

stats = time2.compare_to(time1, 'traceback')
top = stats[0]
print('\n'.join(top.traceback.format()))