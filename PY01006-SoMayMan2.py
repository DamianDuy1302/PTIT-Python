import math
from math import *

if __name__== '__main__':
    
    t = int(input())
    for g in range(t):
        s = input()
        ok=1
        for i in range(len(s)):
            if(s[i]!='4' and s[i]!='7'):
                ok=0
                print('NO')
                break
                
        if(ok==1):
            print('YES')
    