import math
from math import *

def tn(n):
    if(n==n[::-1] and int(n)>9):
        return "YES"
    else: return "NO"

if __name__ == "__main__":
    t = int(input())
    for g in range(t):
        s = input()
        res=0
        for i in range(len(s)):
            res+=int(s[i])
        s = str(res)
        print(tn(s))
        