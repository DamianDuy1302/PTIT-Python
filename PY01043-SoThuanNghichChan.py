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
    
    t = int(input())
    for g in range(t):
        n = int(input())
        for i in range(22, n, 2):
            if(tn(str(i))):
                print(i, end=' ')
        print()
   