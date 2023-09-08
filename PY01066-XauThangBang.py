import math
from math import *

def solve(s1):
        s2 = s1[::-1]
        for i in range(1, len(s1)):
            a1 = ord(s1[i]) - ord(s1[i-1])
            a2 = ord(s2[i]) - ord(s2[i-1])
            if(abs(a1) != abs(a2)):
                return "NO"
        return "YES"

if __name__=="__main__":
    for t in range(int(input())):
        s1 = input()
        print(solve(s1))