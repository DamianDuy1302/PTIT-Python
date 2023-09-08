import math
from math import *

def tn(n):
    tmp=0
    while(n>0):
        tmp = tmp*10+n%10
        n=n//10
    return tmp

def solve(n):
    cnt=0
    res=n
    if(res%7==0):
        return res
    while(True):
        res+=tn(res)
        cnt+=1
        if(res%7==0):
            return res
        if(cnt>1000):
            return -1
    
    
                

if __name__ == '__main__':

    t = int(input())
    for g in range(t):
        n = int(input())
        print(solve(n))
                
           
            
        