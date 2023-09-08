import math
from math import *

def tn(s):
    if len(s) % 2 == 1 or s != s[::-1]:
        return False
    for i in s:
        if int(i) % 2 == 1:
            return False
    return True



if __name__ == '__main__':
    
    t = input()
    print(len(t)-1)