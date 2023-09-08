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
        cnt=0
        for i in range(len(s)):
                cnt+=int(s[i])
        print(nt(cnt))
       
        