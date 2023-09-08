import math
from math import *

def nt(n):
    if(n<2): return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1

if __name__ == "__main__":
    
    n, m = map(int, input().split())
    a=[]
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    for i in range(n):
        for j in range(m):
            
                a[i][j]=nt(a[i][j])
            
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()          