import math
from math import *

def pas(n):
    if(len(n)%2==0):
        n=n+n[0]
    for i in range(2, len(n), 2):
        if(n[i]!=n[i-2]):
            return "NO"
    for i in range(3, len(n)-1, 2):
        if(n[i]!=n[i-2]):
            return "NO"
    return "YES"
    
    
                

if __name__ == '__main__':

    t = int(input())
    for g in range(t):
        n = (input())
        print(pas(n))
                
           
            
        