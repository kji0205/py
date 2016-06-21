import logging
from pprint import pprint
from sys import stdout as STDOUT
import subprocess
from time import sleep, time
import os

def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


proc = run_sleep(10)
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('Exit status', proc.poll())    