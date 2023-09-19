import math
from math import *

class sv:
    def __init__(self, idy, name, lt, th):
        self.id = idy
        self.name = name
        self.lt = lt
        self.th = th
        
        tmp1 = int(lt[:2])
        tmp2 = int(lt[3:])
        tmp3 = int(th[:2])
        tmp4 = int(th[3:])
        
        self.h = tmp3-tmp1
        self.m = tmp4-tmp2
        self.tt = self.h*60+self.m
        self.h = self.tt//60
        self.m = self.tt%60
        
if __name__ == "__main__":
    v=[]
    t = int(input())
    for r in range(t):
        idy = input()
        name = input()
        lt = input()
        th = input()
        a = sv(idy, name, lt, th)
        v.append(a)
    v.sort(key = lambda x:(-x.tt))
    for x in v:
        print(x.id, x.name, x.h, "gio", x.m, "phut")