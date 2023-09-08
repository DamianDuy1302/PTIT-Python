import math
from math import *

def nt(n):
    if(n<2):
        return 0
    else:
        for i in range(2, isqrt(n)+1):
            if(n%i==0):
                return 0
    return 1

p=[1]*1000001

def prime():
    p[0], p[1] = 0, 0
    for i in range(1000):
        if(p[i]==1):
            for j in range(i*i, 1000001, i):
                p[j]=0
            

if __name__ == '__main__':
    prime()
    # for i in range(10, 50):
    #     print(p[i], end=' ')
    t = int(input())
    for h in range(t):
        n = int(input())
        ans=0
        for i in range(n-5):
            if(p[i] and p[i+6]):
                if(p[i+2] or p[i+4]):
                    ans+=1
                    
        print(ans)