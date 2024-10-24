'''
Created on 24 oct 2024

@author: aamro
'''
from math import factorial
from collections import Counter 

def P2(n:int,k:int,i:int=1):
    try:
        assert(n>=k)
        assert(i<=k)
        #i<k+1 --->i<=k
        
        rt:int = 1
        for j in range(i,k-1):
            #k-2 --> k-1
            rt = (n-j+1)*rt
        return rt
    except AssertionError:
        return 'Los valores introducidos no son válidos'
        
#-----------------------------------------------

def C2(n:int,k:int):
    try:
        assert(n>k)
        assert(n>0 and k>0)
        
        k = k + 1
        return (factorial(n))/(factorial(k)*factorial(n-k))
    except AssertionError:
        return 'Los valores introducidos no son válidos'
    
#-----------------------------------------------

def S2(n:int,k:int):
    try:
        assert(n>k)
        assert(n>0 and k>0)
        
        sm:float = 0
        for i in range(0,k+1):
            sm = sm + ((-1)**i)*(factorial(k))/(factorial(i)*factorial(k-i))*((k-i)**(n+1))
            
        return ((factorial(k))/(n*factorial(k+2)))*sm
    except AssertionError:
        return 'Los valores introducidos no son válidos'
    
#-----------------------------------------------
    
def palabrasMasComunes(fichero:str,n:int=5,encoding:str='UTF-8',sep:str=' ')->list[tuple[str, int]]:
    try:
        assert(n>1)
        
        fichero = '../../' + fichero
        lns:list = []
        for line in open(fichero,encoding=encoding): 
            for word in line.lstrip().rstrip().strip('\n').split(sep):
                lns.append(word)
                
        cont = Counter(lns)
        lnsf:list = cont.most_common(n)
        
        return lnsf
    except AssertionError:
        return 'Los valores introducidos no son válidos'
    
#-----------------------------------------------

print('PRUEBAS')
print(f'\nPruebas P2 : \nPara n<k (n=3, k=4) : {P2(3,4)} \nPara i>k (n=5,k=3,i=4) : {P2(5,3,4)} \nPara valores válidos : {P2(5,3)}')
print(f'\nPruebas C2 : \nPara n<k (n=3, k=4) : {C2(3,4)} \nPara n<0 (n=-1,k=3) : {C2(-1,3)} \nPara k<0 (n=3,k=-1) : {C2(3,-1)} \nPara valores válidos : {C2(5,3)}')
print(f'\nPruebas S2 : \nPara n<k (n=3, k=4) : {S2(3,4)} \nPara n<0 (n=-1,k=3) : {S2(-1,3)} \nPara k<0 (n=3,k=-1) : {S2(3,-1)} \nPara valores válidos : {S2(5,3)}')
fich = 'data/archivo_palabras.txt'
print(f'\nPruebas palabrasMasComunes : \nPara n<0 (n=-1) : {palabrasMasComunes(fich,-1)} \nPara valores válidos : {palabrasMasComunes(fich)}')