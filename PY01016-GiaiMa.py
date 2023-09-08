import math
from math import *



if __name__ == '__main__':
    t = int(input())
    for g in range(t):
        s = input()
        ans=""
        for i in range(0, len(s)-1, 2):
            tmp=ord(s[i+1])-ord('0')
            for h in range(tmp):
                ans+=s[i]
        print(ans)