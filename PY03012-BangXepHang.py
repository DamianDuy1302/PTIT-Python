import math
from math import *

class sv:
    def __init__(self, name, ac, submit):
        self.name = name
        self.ac = ac
        self.submit = submit
    
a=[]


if __name__ == "__main__":
    t = int(input())
    for z in range(t):
        x = input();
        y, z = map(int, input().split())
        a.append(sv(x, y, z))
    
    a.sort(key = lambda i:((-1)*i.ac, i.submit, i.name))
    for i in a:
        print('{} {} {}'.format(i.name, i.ac, i.submit))