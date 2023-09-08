import math
from math import *

def solve(n):
    l = list(n)
    maxy = max(l)
    pos = n.find(maxy)
    if(pos==-1 or pos==len(n)-1 or pos==0):
        return "NO"
    for i in range(1, pos+1):
        if(ord(n[i])<=ord(n[i-1])):
            return "NO"
    for i in range(pos+1, len(n)):
        if(ord(n[i])>=ord(n[i-1])):
            return "NO"
    return "YES"

if __name__ == '__main__':
    
    t = int(input())
    for g in range(t):
        n = input()
        print(solve(n))
   