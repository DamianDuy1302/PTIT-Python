import math
from math import *

def nt(n):
    if(len(n)%2==0):
        return "NO"
    if(n[0]==n[1]):
        return "NO"
    for i in range(2, len(n), 2):
        if(n[i]!=n[i-2]):
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for g in range(t):
        s = input()
        print(nt(s))
       
        