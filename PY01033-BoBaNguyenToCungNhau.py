import math
from math import *

def gcd(a, b):
    if(b==0):
        return a
    return gcd(b, a%b)


if __name__ == '__main__':
    
    a, b = map(int, input().split())
    for i in range(a, b+1):
        for j in range(i+1, b+1):
            for k in range(j+1, b+1):
                if(gcd(i, j)==1 and gcd(j, k)==1 and gcd(k, i)==1):
                    print('(', str(i), ', ', str(j), ', ', str(k), ')', sep='')
            
            
        