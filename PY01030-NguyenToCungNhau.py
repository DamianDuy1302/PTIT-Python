import math
from math import *

def gcd(a, b):
    if(b==0):
        return a
    return gcd(b, a%b)


if __name__ == '__main__':
    
    a, b = map(int, input().split())
    cnt=0;
    for i in range(10**(b-1), 10**(b)):
        if(gcd(a, i)==1):
            print(i, end=' ')
            cnt+=1
            if(cnt%10==0):
                print()
            
            
        