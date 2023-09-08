import math
from math import *

def nt(n):
    if(n<2): return 0
    for i in range(2, isqrt(n)+1):
        if(n%i==0):
            return 0
    return 1
p = [2]
for i in range(3, 8000, 2):
    if(nt(i)==1):
        p.append(i)

if __name__ == "__main__":
    
   
    n, x = map(int, input().split())
    print(x, end=' ')
    for i in range(n):
        print(x+p[i], end=' ')
        x = x+p[i]