import math
from math import *

def tcs(n):
    sum=1
    while(n>0):
        sum*=n%10
        n=n//10
    return sum


if __name__ == "__main__":
    
    t = int(input())
    for g in range(t):
        
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        a.sort(key = lambda x:tcs(x))
        for x in a:
            print(x, end=' ')
        print()
        