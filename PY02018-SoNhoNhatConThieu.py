import math
from math import *



if __name__ == "__main__":
    
   
        
        n = int(input())
        a = list(map(int, input().split()))
        ok=1
        miny = min(a)
        maxy = max(a)
        for i in range(miny, maxy+1):
            if i not in a:
                print(i)
                ok=0
                break;
        if(ok==1):
            if(min(a)==1):
                print(max(a)+1) 
            else:
                print(max(a)+1)
                