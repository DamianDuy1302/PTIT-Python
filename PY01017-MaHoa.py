import math
from math import *

if __name__ == '__main__':
    t = int(input())
    for g in range(t):
        s = input()
        s = s+'*'
        ans=""
        pos=0
        while(pos<len(s)-1):
            tmp = s[pos]
            cnt=1
            while(s[pos+1]==tmp):
            
                cnt+=1
                pos+=1
            
            ans+=str(cnt)+tmp
            pos+=1
        print(ans)