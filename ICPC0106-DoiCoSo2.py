import math
from math import log2

BASE = '0123456789ABCDEF'

if __name__ == '__main__':
    t = int(input())
    for g in range(t):
        n = int(input())
        base = int(log2(n))
    #   print(base)
        num = input()
        while(len(num) % base):
            num = '0'+num
            
        pow=[1]
        for i in range(1, base):
            pow = [pow[0]*2]+pow
            
        ans=''
        for i in range(0, len(num), base):
            tmp=0
            for j in range(i, i+base):
                tmp+=int(num[j])*pow[j-i]
                
            ans+=BASE[tmp]
            
        print(ans)
