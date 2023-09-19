import math
from math import *

class sv:
    stt=0
    def __init__(self, name, a):
        sv.stt+=1
        self.id = f'HS{sv.stt:02d}'
        self.name = name
        self.gpa = a[0]*2+a[1]*2
        for i in range(2, 10):
            self.gpa+=a[i]
        self.gpa = self.gpa/10/1.2
        
        if self.gpa>=9.0: self.status="XUAT SAC"
        elif self.gpa>=8.0: self.status="GIOI"
        elif self.gpa>=7.0: self.status="KHA"
        elif self.gpa>=5.0: self.status="TB"
        else: self.status="YEU"
        
    
        

if __name__ == "__main__":
    v = []
    t = int(input())
    for r in range(t):
        name = input()
        a = list(map(float, input().split()))
        tmp = sv(name, a)
        v.append(tmp)
    v.sort(key = lambda x:(-x.gpa, x.id))
    
    for x in v:
        print(x.id, x.name, "%.1f"%round(x.gpa + 0.01, 2) , x.status)
    