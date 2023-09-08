import math
from math import *

if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        
        n = int(input())
        print("1 * ", end='')
        for i in range(2, isqrt(n)+1):
            hat=0
            while(n%i==0):
                hat+=1
                n=n//i
            if(hat!=0):
                if(n>1):
                    print(i, '^', hat, " ", '* ', sep='', end="")
                else:
                    print(i, '^', hat, " ", sep='')
                    
            
        if(n>1):
            print(n, '^1', sep="")
            
            
            
        