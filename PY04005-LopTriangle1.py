import math
from math import *


class point:
    def __init__(self, x, y):
        self.x = (x)
        self.y = (y)
    def dis(self, a):
        d1 = (self.x-a.x)*(self.x-a.x)
        d2 = (self.y-a.y)*(self.y-a.y)
        ans = sqrt(d1+d2)
        return ans
    
class triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def perimeter(self):
        return self.p1 + self.p2 + self.p3
        
    
if __name__ == "__main__":
    t = int(input())
    for g in range(t):
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        
        p1 = point(x1, y1)
        p2 = point(x2, y2)
        p3 = point(x3, y3)
        
        d1 = p1.dis(p2)
        d2 = p2.dis(p3)
        d3 = p3.dis(p1)
        
        delta = triangle(d1, d2, d3)
        
        if(d1+d2>d3 and d2+d3>d1 and d3+d1>d2 and d1>0 and d2>0 and d3>0):
            tmp = delta.perimeter()
            print('%.3f' %tmp)
        else:
            print("INVALID")
        
    