import math
from math import *


def cs(n):
    cnt=0
    while(n>0):
        tmp = n%10
        cnt+=1
        if(tmp!=0 and tmp!=2 and tmp!=4 and tmp!=6 and tmp!=8):
            return 0
        n=n//10
    if(cnt%2==1): return 0
    return 1

def tn(n):
    tmp=n
    res=0
    while(tmp>0):
        res=res*10+tmp%10
        tmp=tmp//10
    if(res==n): return 1
    return 0
    
        


if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        n = int(input())
        for i in range(22, n, 2):        
            if(cs(i)==1 and tn(i)==1):
                print(i, end=' ')
        print()