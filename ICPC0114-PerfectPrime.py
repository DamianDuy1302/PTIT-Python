import math
from math import *

def nt(n):
    if(n<2):
        return 0
    else:
        for i in range(2, isqrt(n)+1):
            if(n%i==0):
                return 0
    return 1
                

def tn(n):
    tmp=0
    while(n>0):
        tmp = tmp*10 + n%10
        n//=10
        
    return tmp

def tcs(n):
    tmp=0
    while(n>0):
        tmp+=n%10
        n//=10
        
    return tmp

     
def csnt(n):
    while(n>0):
        tmp = n%10
        if(tmp!=2 and tmp!=3 and tmp!=5 and tmp!=7):
            return 0
        n//=10
    return 1    

def passi(n):
    if(nt(n)==0 or csnt(n)==0 or nt(tcs(n))==0 or nt(tn(n))==0):
        return 0
    return 1      

if __name__ == '__main__':

    
    t = int(input())
    for h in range(t):
        n = int(input())
        if(passi(n)==0):
            print('No')
        else:
            print("Yes")