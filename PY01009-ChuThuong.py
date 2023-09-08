import math
from math import *

if __name__== '__main__':
    
    s = input()
    tmp = s.lower()
    cnt=0
    for i in range(len(s)):
        if(tmp[i]==s[i]):
            cnt+=1
            
    if(cnt<len(s)/2):
        print(s.upper())
    else:
        print(tmp)
    