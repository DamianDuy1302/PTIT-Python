import math
from math import *

if __name__ == '__main__':
    
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
 
    while(True):
        str = input()
        if(str=='0'):
            break
        
            
        else:
            k, s = str.split()
            k = int(k)
            ans=""
            for i in s:
                j = base.find(i)
                ans+=base[(j+k)%28]
            
            print(ans[::-1])