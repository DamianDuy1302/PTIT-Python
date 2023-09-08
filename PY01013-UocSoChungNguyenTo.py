import math
from math import *


def gcd(a, b):
    if(b==0): return a
    else: return gcd(b, a%b)
    
def nt(n):
    if(n<2): return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1
def tcs(n):
    ans=0;
    while(n>0):
        ans+=n%10
        n=n//10
    return ans


if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        a, b = map(int, input().split())
        tmp = gcd(a, b)
        if(nt(tcs(tmp))==1):
            print("YES")
        else:
            print("NO")