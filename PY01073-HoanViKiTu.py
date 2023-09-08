import math
from math import *

n = input()
f = [0] * 15

def tryy(s):
    if(len(s)==len(n)):
        print(s)
        return
    
    else:
        for j in range(len(n)):
            if(f[j]==0):
                
                f[j]=1
                tryy(s+n[j])
                f[j]=0
    
tryy('')