import math
from math import *


if __name__ == '__main__':
    t = int(input())
    d = dict({})
    for g in range(t):
        s = input()
        if(s in d):
            d[s]+=1
        else:
            d[s]=1
            
    print(len(d))
        