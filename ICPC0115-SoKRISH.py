import math
from math import *



if __name__ == '__main__':
    t = int(input())
    for h in range(t):
        n = int(input())
        tmp = n
        a=[]
        while(tmp>0):
            a.append(tmp%10)
            tmp//=10
        b = [factorial(x) for x in a]
        tmp = sum(b)
        if(n==tmp):
            print('Yes')
        else:
            print('No')
        