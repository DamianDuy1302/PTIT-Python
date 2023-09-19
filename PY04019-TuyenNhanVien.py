import math
from math import *

class sv:
    stt=0
    def __init__(self, name, lt, th):
        sv.stt+=1
        self.id = "TS0" + str(sv.stt)
        self.name = name
        # self.lt = lt
        # self.th = th
        
        if(lt > 10): lt/=10
        if(th > 10): th/=10
        self.ave = (lt+th)/2
        if(self.ave>9.5): self.status = "XUAT SAC"
        elif(self.ave>=8): self.status = "DAT"
        elif(self.ave>=5): self.status = "CAN NHAC"
        else: self.status = "TRUOT"
        

if __name__ == "__main__":
    v=[]
    t = int(input())
    for r in range(t):
        name = input()
        lt = float(input())
        th = float(input())
        a = sv(name, lt, th)
        v.append(a)
    
    v.sort(key = lambda x:(-x.ave))
    for x in v:
        print(x.id, x.name, "%.2f"%x.ave, x.status)
    