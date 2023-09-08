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
   
        a = list(map(int, input().split()))
        cnt=0
        for i in range(1, len(a)):    
            if(a[i]!=a[i-1]):
                cnt+=1
        print(cnt)