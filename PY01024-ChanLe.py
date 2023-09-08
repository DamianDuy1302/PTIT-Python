import math
from math import *


def tcs10(s):
    tcs=0
    for i in range(len(s)):
        tcs+=ord(s[i])-ord('0')
    
    if(tcs%10==0): return 1
    return 0

def cs2(n):
    for i in range(1, len(n)):
        if abs(ord(n[i])-ord(n[i-1]))!=2:
            return 0
    return 1

if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        
        s = input()
        
        if(tcs10(s)==1 and cs2(s)==1):
            print("YES")
        else:
            print("NO")
            
            
            
        