import math
from math import *





if __name__ == '__main__':
    t = int(input())
    for h in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        res = 0
        for i in range(n-2):
            l=i+1
            r=n-1
            while(l<r):
                tmp = a[i]+a[l]+a[r]
                if(tmp==0):
                    res+=1
                    l+=1                    
                elif tmp<0:
                    l+=1
                else:
                    r-=1
                    
        print(res)