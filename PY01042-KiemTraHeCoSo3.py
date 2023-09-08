import math
from math import *

def solve(n):
    for i in range(len(n)):
        if(n[i]!='0' and n[i]!='1' and n[i]!='2'):
            return "NO"
    return "YES"

if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        n = input()
        print(solve(n))
   