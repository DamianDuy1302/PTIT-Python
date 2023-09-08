import math
from math import *


class ps:
    def __init__(self, t, m):
        self.t = int(t)
        self.m = int(m)
    
    def rutgon(self):
        tmp = math.gcd(self.t, self.m)
        self.t = int(self.t/tmp)
        self.m = int(self.m/tmp)
    

if __name__ == "__main__":
    t, m = map(int, input().split())
    a = ps(t, m)
    a.rutgon()
    print(a.t, '/', a.m, sep='')
    