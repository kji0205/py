import os
import time

path = b'C:\inetpub\logs\LogFiles\W3SVC2\u_ex160613.log'

if os.path.exists(path):
    # print('T')
    while True:
        time.sleep(3)
        f = open(path, 'rt')
        data = f.read()
        f.close()
        print(data)

# tmr = TimerClass()
