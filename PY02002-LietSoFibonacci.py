import math
from math import *

f = [0]*93
def pre():
    f[1]=1
    f[2]=1
    for i in range(3, 93):
        f[i]=f[i-1]+f[i-2]

if __name__ == "__main__":
    pre()
    t = int(input())
    for g in range(t):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            print(f[i], end=' ')
        print()