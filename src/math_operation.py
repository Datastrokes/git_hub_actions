import os
import sys
print(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))
def add (a,b):
    return a+b
def sub (a,b):
    return a-b