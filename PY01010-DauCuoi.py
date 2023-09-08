import math
from math import *

if __name__== '__main__':
    
    t = int(input())
    for g in range(t):
        s = input()
        s1 = s[0]+s[1]
        s2 = s[len(s)-2] + s[len(s)-1]
        if(s1==s2):
            print('YES')
        else:
            print('NO')
    