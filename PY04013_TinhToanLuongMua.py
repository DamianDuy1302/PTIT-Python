import math
from math import *

def cal_hour1(self1, self2):
        tmp1 = int(self1[:2])
        tmp2 = int(self1[3:])
        tmp3 = int(self2[:2])
        tmp4 = int(self2[3:])
        minute = ((tmp3-tmp1)*60 + (tmp4-tmp2))/60       
        return minute

class des:
    stt = 0
    def __init__(self, name, start, end, amount):
        des.stt+=1
        self.name = name
        self.start = start
        self.end = end
        self.amount = amount
        self.m = self.cal_hour()
        self.id = f'T{des.stt:02d}'
    
    def cal_hour(self):
        tmp1 = int(self.start[:2])
        tmp2 = int(self.start[3:])
        tmp3 = int(self.end[:2])
        tmp4 = int(self.end[3:])
        minute = ((tmp3-tmp1)*60 + (tmp4-tmp2))/60       
        return minute
    def average_rain(self):
        return self.amount/self.m
    
if __name__ == "__main__":
    v = []
    d = dict({})
    t = int(input())
    for r in range(t):
        name = input()
        timein = input()
        timeout = input()
        amount = int(input())
        if name in d:
            m = cal_hour1(timein, timeout)
            for x in v:
                if x.name == name:
                    x.m+=m
                    x.amount+=amount
                    
        else:
            a = des(name, timein, timeout, amount)
            v.append(a)
            d[name]=1
            
    for x in v:
        print(x.id, x.name, end=' ')
        print("%.2f" %x.average_rain())
            
        