import os

try:
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
    with open('somefile', 'xb') as f:
        f.write('Hello\n')
    pass
except Exception:
    print('Exception')

if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File a already exists')
