import math
from math import *

def nt(n):
    if(n<2): return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1


if __name__ == "__main__":
    
   
        
        n = int(input())
        a = list(map(int, input().split()))
        
        d = dict({})
        for x in a:
            if(nt(x)==1):
                if(x in d):
                    d[x]+=1
                else:
                    d[x]=1
        for x in d:
            print(x, d[x])  