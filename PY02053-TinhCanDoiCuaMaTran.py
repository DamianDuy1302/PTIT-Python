import math
from math import *

if __name__ == "__main__":
    n = int(input())
    a=[]
    for t in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    k = int(input())
    up=0
    do=0
    for i in range(n):
        for j in range(n):
            if(i==n-j-1): continue
            elif(i<n-j-1): up+=a[i][j]
            else: do+=a[i][j]
            
    tmp = abs(up-do)
    if(tmp <= k): print("YES")
    else: print("NO")
    print(tmp)
    