'''
Created on 3 oct 2024

@author: aamro
'''
from fp.funciones import *

print('\nPRODUCTORIO')
n1:int = 1
k1:int = 1

while n1<=k1 :
    n1 = int(input('n = '))
    k1 = int(input('k = '))
    if n1<=k1 :
        print('n es menor o igual a k, por favor, introduzca valores válidos')
        
print(f'El productorio con de ({n1} -i +1) con {k1} repeticiones es: {fun1(n1,k1)}')

#----------------------------------------------------------------------------

print('\nPRODUCTO DE SECUENCIA GEOMÉTRICA')
a2 = int(input('a1 = '))
r2 = int(input('r = '))
k2 = int(input('k = '))

def sec(k2) :
    ls:list = []
    for i in range(0, k2) :
        ls.append(f'a({i+1})')
    return ' · '.join(ls)

print(f'{sec(k2)} = {fun2(a2,r2,k2)}')

#----------------------------------------------------------------------------

print('\nNÚMERO COMBINATORIO')
n3:int = 1
k3:int = 1

while n3<=k3 :
    n3 = int(input('n = '))
    k3 = int(input('k = '))
    if n3<=k3 :
        print('n es menor o igual a k, por favor, introduzca valores válidos')

print(f'El número combinatorio de {n3} y {k3} es: {fun3(n3,k3)}')

#----------------------------------------------------------------------------

print('\nSUMATORIO Y NÚMERO COMBINATORIO')
n4:int = 1
k4:int = 1

while n4<=k4 :
    n4 = int(input('n = '))
    k4 = int(input('k = '))
    if n4<=k4 :
        print('n es menor o igual a k, por favor, introduzca valores válidos')

print(f'El número S(n,k) siendo n = {n4} y k = {k4} es: {fun4(n4,k4)}')

#----------------------------------------------------------------------------

print('\nMÉTODO DE NEWTON')
a5 = float(input('a = '))
e5 = float(input('Error = '))

f = lambda a : a**2 + 2*a + 1
f_tx:str = 'x^2 + 2x + 1'
fd = lambda a : 2*a + 2
fd_tx:str = '2x + 2'

print(f'El resultado del método de Newton de f(x) = {f_tx} y f´(x) = {fd_tx} con x0 = {a5} y error <= {e5} es : {fun5(a5, e5, f, fd)}')
