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
                if(i==n-1-j): continue
                elif(j>n-i-1):
                    up+=a[i][j]
                elif(j<n-i-1):
                    do+=a[i][j]
                    
        ans = abs(up-do)
        if(ans<=k): print("YES")
        else: print("NO")
        print(abs(ans))            
        
        
        