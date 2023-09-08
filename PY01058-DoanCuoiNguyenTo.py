import math
from math import *

def nt(n):
    if(n<2): return "NO"
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for g in range(t):
        s = input()
        tmp =""
        for i in range(len(s)-4, len(s)):
            tmp+=s[i]
       
        n = int(tmp)
       
        print(nt(n))
        