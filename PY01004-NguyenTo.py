import math
from math import *

def nt(n):
    if(n<2):
        return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1

def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)

if __name__== '__main__':
    
    t = int(input())
    for h in range(t):
        n = int(input())
        cnt=0
        tmp=0
        for g in range(1, n):
            if(gcd(g, n)==1):
                tmp+=1
                
        if(nt(tmp)==1):
            print('YES')
        else:
            print('NO')
                