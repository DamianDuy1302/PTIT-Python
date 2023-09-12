import math
from math import *


class sp:
    def __init__(self, r, i):
        self.r = r;
        self.i = i;

    def congsp(self, a):
        r1 = self.r + a.r
        i1 = self.i + a.i
        return sp(r1, i1)
    
    def nhansp(self, a):
        r1 = self.r*a.r - self.i*a.i
        i1 = self.i*a.r + self.r*a.i
        return sp(r1, i1)
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b, c, d = map(int, input().split())
        A = sp(a, b)
        B = sp(c, d)
        E = A.congsp(B)
        C = E.nhansp(A)
        D = E.nhansp(E)
        if(C.i < 0):
            
            print(C.r, ' - ', -(C.i), 'i', end=', ', sep="")
        else: 
            print(C.r, ' + ', (C.i), 'i', end=', ', sep="")
        if(D.i < 0):            
            print(D.r, ' - ', -(D.i), 'i', sep="")
        else: 
            print(D.r, ' + ', (D.i), 'i', sep="")   
        