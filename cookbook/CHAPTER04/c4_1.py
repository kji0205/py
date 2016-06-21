'''수동으로 이터레이터 소비'''
# import os


# with open('./etc/passwd') as f:
#     try:
#         while True:
#             line = next(f)
#             print(line, end='')
#     except StopIteration:
#         pass

# with open('./etc/passwd') as f:
#     while True:
#         line = next(f, None)
#         if line is None:
#             break
#         print(line, end='')

items = [1, 2, 3]
it = iter(items)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
