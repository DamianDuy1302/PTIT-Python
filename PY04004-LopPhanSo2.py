import math
from math import *


class ps:
    def __init__(self, t, m):
        self.t = (t)
        self.m = (m)
    
    def rutgon(self):
        tmp = math.gcd(self.t, self.m)
        self.t = int(self.t//tmp)
        self.m = int(self.m//tmp)
        return self
    
    def congps(self, a):
        mau = self.m*a.m // math.gcd(self.m, a.m)
        res = ps(self.t * mau//self.m + a.t*mau//a.m, mau)
        return res.rutgon()

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    A = ps(a, b)
    B = ps(c, d)
    C = A.congps(B)
    
    print(str(C.t)+'/'+str(C.m), sep='')
    