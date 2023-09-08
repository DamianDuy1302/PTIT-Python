import math
from math import *

def cunghoangdao(a, b):
    if(a>=21 and b==3) or (a<=19 and b==4):
        return "Bach Duong"
    if(a>=20 and b==4) or (a<=20 and b==5):
        return "Kim Nguu"
    if(a>=21 and b==5) or (a<=20 and b==6):
        return "Song Tu"
    if(a>=21 and b==6) or (a<=22 and b==7):
        return "Cu Giai"
    if(a>=23 and b==7) or (a<=22 and b==8):
        return "Su Tu"
    if(a>=23 and b==8) or (a<=22 and b==9):
        return "Xu Nu"
    if(a>=23 and b==9) or (a<=22 and b==10):
        return "Thien Binh"
    if(a>=23 and b==10) or (a<=22 and b==11):
        return "Thien Yet"
    if(a>=23 and b==11) or (a<=21 and b==12):
        return "Nhan Ma"
    if(a>=22 and b==12) or (a<=19 and b==1):
        return "Ma Ket"
    if(a>=20 and b==1) or (a<=18 and b==2):
        return "Bao Binh"
    if(a>=19 and b==2) or (a<=20 and b==3):
        return "Song Ngu"

if __name__ == '__main__':
    t = int(input())
    for h in range(t):
        a, b = map(int, input().split())
        print(cunghoangdao(a, b))