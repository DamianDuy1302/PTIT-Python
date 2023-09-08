import math
from math import *

if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        
        s = input()
        if(s[len(s)-2]!='8' or s[len(s)-1]!='6'):
            print("NO")
        else:
            print("YES")
            
            
        