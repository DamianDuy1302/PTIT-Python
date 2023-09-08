import math
from math import *

def nt(n):
    if(n<2): return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1

if __name__ == "__main__":
    t = int(input())
    for g in range(t):
        s = input()
        s1, s2 = "", ""
        for i in range(0, 3):
            s1+=s[i]
        for i in range(len(s)-3, len(s)):
            s2+=s[i]
        if(nt(int(s1))==1 and nt(int(s2))==1):
            print("YES")
        else:
            print("NO")
        