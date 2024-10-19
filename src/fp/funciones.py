'''
Created on 3 oct 2024

@author: aamro
'''
from typing import Callable
import math

def fun1(n:int,k:int) -> int:
    rt:int = 1
    for i in range(0,k):
        rt = (n-i+1)*rt
    return rt

def fun2(a1:int,r:int,k:int) -> int:
    rt:int = 1
    for i in range (0,k) :
        rt = a1*(r**i)*rt
    return rt
#range(1,k+1) , (i-1) ---> range(0,k) , (i)

def fun3(n:int,k:int) -> int:
    return (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))

def fun4(n:int,k:int) -> float:
    s:float = 0.
    for i in range(0,k):
        s = s + ((-1)**i)*(fun3(k+1,i+1))*((k-i)**n)
    return s/(math.factorial(k))

def fun5(a:float,e:float,f:Callable[[float],float],fd:Callable[[float],float]) -> float:
    while (abs(f(a))>e):
        a = a - (f(a)/fd(a))
    return a

def fun6(file:str,cad:str,sep:str,encoding:str='UTF-8') -> int:
    i:int = 0
    for line in open(file,encoding=encoding): 
        for word in line.split(sep):
            if cad.lower() == word.lower():
                i += 1
    return i

def fun7(file:str,cad:str,encoding:str='UTF-8') -> list:
    lns:list = []
    for line in open(file,encoding=encoding): 
        if cad.lower() in line.lower():
            lns.append(line.lstrip().rstrip().strip('\n'))
    return lns

def fun8(file:str,encoding:str='UTF-8') -> list:
    lns:list = []
    sep:str = ' '
    
    if file[-3:] == 'csv':
        sep = ','
    
    for line in open(file,encoding=encoding): 
        for word in line.strip('\n').split(sep):
            new_word:bool = True
            for i in lns:
                if word.lower() == i.lower():
                    new_word = False    
            if new_word and (len(word.strip()) != 0):
                lns.append(word)
    return lns

def fun9(file:str,encoding:str='UTF-8') -> float:
    sep:str = ' '
    line_num:int = 0
    word_num:int = 0
    
    if file[-3:] == 'csv':
        sep = ','
        
    for line in open(file,encoding=encoding): 
        lns:list = []
        for word in line.lstrip().rstrip().strip('\n').split(sep):
            lns.append(word)
        line_num += 1
        word_num += len(lns)
    
    try : 
        return word_num/line_num
    except ZeroDivisionError :
        return None
