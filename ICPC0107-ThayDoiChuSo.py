import math
from math import *


if __name__ == '__main__':
    
    t = int(input())
    for h in range(t):
        n, m = input().split()
        ip = input().split()
        print(ip)
        if len(ip) == 1:
            a = ip[0]
            b = input()
        else:
            a, b = ip
            
        #neu nhap tren 2 dong thi so dau tien la a, so thu hai la b
        #neu nhap 1 dòng thì ip sẽ có 2 thành phần
        #a, b = ip nghĩa la a = ip[0], b = ip[1]
        ans_1 = int(a.replace(n, m)) + int(b.replace(n, m)) 
        ans_2 = int(a.replace(m, n)) + int(b.replace(m, n)) 
        
        # ans_max = int(maxy(a)) + int(maxy(b))
        # ans_min = int(miny(a)) + int(miny(b))
        # print(ans_min, ans_max)
        print(min(ans_1, ans_2), max(ans_1, ans_2))