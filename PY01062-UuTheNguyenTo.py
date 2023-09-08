import math
from math import *

def nt(n):
    if(n<2): return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1

def solve(s):
        l = list(s)
        n = list(filter(lambda x:nt(int(x))==1, l))
        
        if(nt(len(s))==1):            
            if(len(n)>len(s)/2):
                return("YES")
                    
        
        return("NO")

if __name__ == "__main__":
    t = int(input())
    for g in range(t):
        s = input()
        print(solve(s))
        