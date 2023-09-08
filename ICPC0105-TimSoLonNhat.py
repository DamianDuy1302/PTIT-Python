import math
from math import *

def ischar(n):
    if(n>='0' and n<='9'):
        return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    
    for h in range(n):
        s = input()
        s = s +'z' 
              
        a = []
        pos=0
        tmp=0
        while(pos<len(s)):
            if(ischar(s[pos])==1):
                while(ischar(s[pos])==1):
                    tmp = tmp*10 + (ord(s[pos])-ord('0'))
                    pos+=1
            
            if(tmp!=0):
                a.append(tmp)
            tmp=0
            pos+=1
        
            
        
        print(max(a))
        