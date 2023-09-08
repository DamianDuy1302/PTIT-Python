import math
from math import *




if __name__ == '__main__':
    
    s = input()
    tmp = s[::-1]
    ans=list([])
    pos=0
    cnt=1
    res=""
    while(pos<len(tmp)):
        res+=tmp[pos]
        if(cnt==3 or pos==len(tmp)-1):
            ans.append(res[::-1])
            cnt=1
            res=""
        else: cnt+=1
        pos+=1
    ans = ans[::-1]
    print(','.join(ans))
    
            
            
            
        