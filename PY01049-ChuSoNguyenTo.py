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
        cnt=0
        for i in range(len(s)):
            if(nt(int(s[i]))==1):
                cnt+=1
        if(nt(len(s))==0 or cnt<=len(s)//2):
            print("NO")
        else:
            print("YES")
       
        