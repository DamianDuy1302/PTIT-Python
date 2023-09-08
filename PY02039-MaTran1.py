import math
from math import *



if __name__ == "__main__":
    
    
        
        n = int(input())
        a = []
        for i in range(n):
            b = list(map(int, input().split()))
            a.append(b)         
        k = int(input())
        
        up, do = 0, 0
        for i in range(0, n):
            for j in range(0, n):
                if(i==j): continue
                elif(i<j):
                    up+=a[i][j]
                else:
                    do+=a[i][j]
                    
        ans = abs(up-do)
        if(ans<=k): print("YES")
        else: print("NO")
        print(abs(ans))            
        
        
        