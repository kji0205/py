import os

path = 'D:/Repo/py/cookbook/CHAPTER05/data.csv'
path2 = 'D:/Repo/py/cookbook/CHAPTER05/data'
path3 = 'D:/Repo/py/cookbook/CHAPTER05/'
path4 = 'D:/Repo/py/cookbook/CHAPTER05/data - Shortcut'
path5 = 'D:/Repo/py/cookbook/CHAPTER05/c5_12.py'

print(os.path.exists(path))
print(os.path.exists(path2))

print(os.path.isfile(path))
print(os.path.isfile(path2))

print(os.path.isdir(path))
print(os.path.isdir(path2))
print(os.path.isdir(path3))

print(os.path.islink(path3))

print(os.path.realpath(path4))

if os.path.isfile(path5):
    print(os.path.getsize(path5))
    print(os.path.getmtime(path5))
    import time
    print(time.ctime(os.path.getmtime(path5)))


