import math
from math import *

def gcd(a, b):
    if(b==0): return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b/gcd(a, b)

def nt(n):
    if(n<2): return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1

if __name__ == "__main__":
    n = int(input())
    for g in range(n):
        a, b = map(int, input().split())
        sum = factorial(b) // factorial(a-1)
        if(nt(sum)==1):
            print(3)
        else:
            
            cnt=0
            for i in range(1, sum):
                if(sum%i==0):
                    cnt+=3
                    if(cnt>=(10**9+7)):
                        cnt = cnt%(10**9+7)
            print(cnt)