import math
from math import *

def tcs(n):
    sum=0
    while(n>0):
        sum+=n%10
        n=n//10
    return sum


if __name__ == "__main__":
    
    t = int(input())
    for g in range(t):
        
        n = int(input())
        a = list(map(int, input().split()))
        
        a.sort(key = lambda x:(tcs(x), x))
        for x in a:
            print(x, end=' ')
        print()
        