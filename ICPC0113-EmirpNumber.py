import math
from math import *

def tn(n):
    tmp=0
    while(n>0):
        tmp = tmp*10 + n%10
        n//=10
        
    return tmp

p=[1]*1000001

def prime():
    p[0], p[1] = 0, 0
    for i in range(1000):
        if(p[i]==1):
            for j in range(i*i, 1000001, i):
                p[j]=0
            

if __name__ == '__main__':
    prime()
    # for i in range(10, 50):
    #     print(p[i], end=' ')
    t = int(input())
    for h in range(t):
        n = int(input())
        a=[]
        for i in range(13, n+1):
            tmp = tn(i)
            if(p[i]==1 and p[tmp]==1 and i!=tmp and i<=n and tmp<=n):
                if(i not in a):
                    a.append(i)
                    a.append(tmp)
        for x in a:
            print(x, end=' ')
        print()