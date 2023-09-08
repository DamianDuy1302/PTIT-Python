import math
from math import *



if __name__ == "__main__":
    
    t = int(input())
    for g in range(t):
        
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        d = dict({})
        maxy=0
        ans=1000005
        for x in a:
            if(x in d):
                d[x]+=1    
            else:
                d[x]=1
                
        for x in d:       
            if(maxy < d[x]):
                maxy = d[x]
                ans =  x
      
        if(maxy <= n//2):
            print("NO")
        else:
            print(ans)