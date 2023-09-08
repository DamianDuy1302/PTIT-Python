import math
from math import *



if __name__ == "__main__":
    
    t = int(input())
    for g in range(t):
        
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        ok=0
        for i in range(n):
            if(a[i]>b[i]):
                print("NO")
                ok=1
                break
        if(ok==0):
            print("YES")