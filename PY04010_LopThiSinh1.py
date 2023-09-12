import math
from math import *


class sp:
    def __init__(self, name, bd, d1, d2, d3):
        self.name = name
        self.bd = bd
        self.d1 =d1
        self.d2 = d2
        self.d3 =d3

    def tt(self):
        return self.d1 + self.d2 + self.d3
    
    
    
if __name__ == "__main__":
    
    
        name = input()
        bd = input()
        d1 = float(input())
        d2 = float(input())
        d3 = float(input())
        
        a = sp(name, bd, d1, d2, d3)
        tt = a.tt()
        print(a.name, a.bd, tt)
        