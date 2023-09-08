import math
from math import *

def nt(n):
    if(n<2): return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1

def solve(s):
    for i in range(len(s)):
            ti = int(s[i])
            if(nt(ti)==1 and nt(i)==0) or (nt(ti)==0 and nt(i)==1):
                return "NO"
    return "YES"
                
                

if __name__ == "__main__":
    t = int(input())
    for g in range(t):
        s = input()
        print(solve(s))
        
        
       
        