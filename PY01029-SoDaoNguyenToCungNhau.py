import math
from math import *

def gcd(a, b):
    if(b==0):
        return a
    return gcd(b, a%b)


if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        n = (input())
        n1 = n[::-1]
        a = int(n)
        b = int(n1)
        if(gcd(a, b)==1): print("YES")
        else:
            print('NO')
            
            
        