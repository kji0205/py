import os
path = 'D:/Repo/py/cookbook/CHAPTER05/data.csv'

print(os.path.basename(path))

print(os.path.dirname(path))

print(os.path.join('tmp', 'data', os.path.basename(path)))

path = '~/Data/data.csv'
print(os.path.expanduser(path))

print(os.path.splitext(path))
