import sys
import os

print(sys.getfilesystemencoding())

path = 'D:/Repo/py/cookbook/CHAPTER05'

# with open(path + '\jalape\xf1o.txt', 'w') as f:
#     f.write('Spicy!')

# print(os.listdir(path))
filename = os.listdir(path)

def bad_filename(filename):
    return repr(filename)[1:-1]

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))
