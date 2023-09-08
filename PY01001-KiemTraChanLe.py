import math
from math import *

if __name__== '__main__':
    
    s = input()
    c = s[len(s)-1]
    if(c=='0' or c=='2' or c=='4' or c=='6' or c=='8'):
        print('CHAN')
    else:
        print('LE')