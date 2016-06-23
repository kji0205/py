import os

path = 'D:/Repo/py/cookbook/'
names = os.listdir(path)
# print(names)

names = [name for name in os.listdir(path)
         if os.path.isfile(os.path.join(path, name))]
print(names)

names = [name for name in os.listdir(path)
         if os.path.isdir(os.path.join(path, name))]
print(names)

pyfiles = [name for name in os.listdir(path)
           if name.endswith('.py')]
print(pyfiles)

import glob

pyfiles = glob.glob(path + '*.py')
print(pyfiles)

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir(path)
           if fnmatch(name, '*.py')]
print(pyfiles)

import os.path
pyfiles = glob.glob('*.py')

name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
