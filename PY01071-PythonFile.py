import math
from math import *

def solve(s1):
    n = ".py"
    s1 = s1.lower()
    id = s1.find(n)
    if(id==-1):
        return "no"
    return 'yes'

if __name__=="__main__":
    
        s1 = input()
        print(solve(s1))