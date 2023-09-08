import math
from math import *

if __name__=="__main__":
    for t in range(int(input())):
        s = input()
        n = input()
        l, id, cnt = len(n), s.find(n), 0
        while id != -1:
            cnt += 1
            id = s.find(n, id + l)
        print(cnt)