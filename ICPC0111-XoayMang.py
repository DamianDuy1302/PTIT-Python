import math
from math import *



if __name__ == '__main__':
    t = int(input())
    for h in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        while(k>=n):
            k-=n
        
        for i in range(k, n):
            print(a[i], end=' ')
        for i in range(k):
            print(a[i], end=' ')
        print()