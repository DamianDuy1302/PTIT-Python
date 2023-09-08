import math
from math import *

def ntt(n):
    if(n<2): return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1

def nt(n):
    if(len(n)%2==1):
        n=n+'0'
    cnt=0
    for i in range(0, len(n)-1, 2):
        if(int(n[i])%2==1):
            return "NO"
        cnt+=int(n[i])
    for i in range(1, len(n), 2):
        if(int(n[i])%2==0):
            return "NO"
        cnt+=int(n[i])
    if(ntt(cnt)==0):
        return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for g in range(t):
        s = input()
        print(nt(s))
       
        