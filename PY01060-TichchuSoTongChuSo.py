import math
from math import *

def solve(s):
    sumc=0
    suml=1
    checkl=0
    for i in range(len(s)):
        if(i%2==1):
            sumc+=int(s[i])
        else:
            if(s[i]!='0'):
                if(s[i]=='1'):
                    checkl=1
                suml*=int(s[i]) 
    
    if(checkl==0 and suml==1):
        print(0, end=' ')
    else:
        print(suml, end=' ')      
    print(sumc)
if __name__ == "__main__":
    t = int(input())
    for g in range(t):
        s = input()
        solve(s)
       
        
        