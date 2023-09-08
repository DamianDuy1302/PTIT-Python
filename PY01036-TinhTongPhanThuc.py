import math
from math import *

def gcd(a, b):
    if(b==0):
        return a
    return gcd(b, a%b)


if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        n = int(input())
        sum=0
        if(n%2==0):
            for h in range(2, n+1, 2):
                sum+=1/h
                
        else:        
            for h in range(1, n+1, 2):
                sum+=1/h 
        print("%.6f" %sum)
            
        