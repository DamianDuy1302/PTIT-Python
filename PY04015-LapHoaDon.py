import math
from math import *

class client:
    stt = 0
    def __init__(self, name , inn, outt):
        client.stt+=1
        self.id = f'KH{client.stt:02d}'
        self.name = name
        cnt = outt - inn
        if(cnt<=50):
            self.payment = (100*cnt) *1.02
        elif(cnt<=100):
            self.payment = (50*100 + (cnt-50)*150)*1.03
        else:
            self.payment = (50*100 + 50*150 + (cnt-100)*200)*1.05
            
        self.payment = round(self.payment)

if __name__ == "__main__":
    v=[]
    t = int(input())
    for r in range(t):
        name = input()
        inn = int(input())
        outt = int(input())
        a = client(name, inn, outt)
        v.append(a)
    v.sort(key = lambda x:-x.payment)
    for x in v:
        print(x.id, x.name, int(x.payment))