import math
from math import *

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
l = []

for i in arr:
    if i not in l:
        l.append(i)

l.sort()
n = len(l)
a = [0]*(n+1)
ans = [0]*(k+1)

def inkq1():
    for i in range(1, k+1):
        print(a[i], end=' ')
    print()
    
def inkq():
    for i in range(1, k+1):
        print(ans[i], end=' ')
    print()


def tryy(i):
    for j in range(a[i-1]+1, n-k+i+1):
        a[i] = j    
        ans[i] = l[j-1]
        if(i==k):
            inkq()
         
        else:
            tryy(i+1)
            
           
tryy(1)