import math
from math import *

if __name__== '__main__':
    
    t = int(input())
    for g in range(t):
        
        n, x, m = map(float, input().split())
        y=0
        while(n<m):
            y+=1
            n = n + n*x/100
        print(y)
    