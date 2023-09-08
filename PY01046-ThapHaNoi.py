import math
from math import *

def tn(n, a, b, c):
    if(n==1):
        print(a, '->', c)
        return
    tn(n-1, a, c, b)
    tn(1, a, b, c)
    tn(n-1, b, a, c)
    



if __name__ == '__main__':
    
    t = int(input())
    tn(t, 'A', 'B', 'C')
    