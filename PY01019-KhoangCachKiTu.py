import math
from math import *

if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        
        s1 = input()
        s2 = s1[::-1]   
        ok=0
        for i in range(1, len(s1)):
            
            a1 = abs(ord(s1[i]) - ord(s1[i-1]))
            a2 = abs(ord(s2[i]) - ord(s2[i-1]))
            if(a1!=a2):
                print("NO")
                ok=1
                break
        if(ok==0):
            print("YES")
            
            
        