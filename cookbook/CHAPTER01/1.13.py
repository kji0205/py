"""일반 키로 딕셔너리 리스트 정렬"""
from operator import itemgetter
from time import time
print(time())

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]

start = time()
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
end = time()
# print(rows_by_fname)
# print(rows_by_uid)
print('itemgetter: Took %.33f seconds' % (end - start))

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
# print(rows_by_lfname)

start = time()
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
# print(rows_by_fname)
# print(rows_by_lfname)
end = time()
print('Lambda: Took %.33f seconds' % (end - start))
print(time())

print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))
