import math
from math import *

if __name__== '__main__':
    
    s = input()
    l = s.split()
    
    a = l[0]
    b = l[2]
    c = l[4]
    oper = l[1]
    
    if(oper=='+'):
        if(int(a)+int(b)==int(c)):
            print('YES')
        else:
            print('NO')
            
    elif(oper=='-'):
        if(int(a)-int(b)==int(c)):
            print('YES')
        else:
            print('NO')
    elif(oper=='*'):
        if(int(a)*int(b)==int(c)):
            print('YES')
        else:
            print('NO')
    elif(oper=='/'):
        if(int(a)//int(b)==int(c)):
            print('YES')
        else:
            print('NO')