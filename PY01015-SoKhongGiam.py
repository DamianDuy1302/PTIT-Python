import math
from math import *



if __name__ == '__main__':
    t = int(input())
    for g in range(t):
        s = input()
        ok=1
        for i in range(1, len(s)):
            if(ord(s[i])<ord(s[i-1])):
                print("NO")
                ok=0
                break
        if(ok==1):
            print("YES")