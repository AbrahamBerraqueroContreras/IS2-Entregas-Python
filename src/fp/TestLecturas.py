'''
Created on 17 oct 2024

@author: aamro
'''

from fp.funciones import *

print('\nREPETICIÓN DE PALABRAS')
path1:str = input('Introduzca la dirección del archivo : ')
cad1:str = input('Introduzca una palabra : ')
sep1:str = input('Introduzca un separador : ')
pathn1:str = '../../' + path1

print(f'La palabra {cad1} apararece {fun6(pathn1,cad1,sep1)} veces en {path1}')

#----------------------------------------------------------------------------

print('\nPALABRA EN LÍNEAS')
path2:str = input('Introduzca la dirección del archivo : ')
cad2:str = input('Introduzca una palabra : ')
pathn2:str = '../../' + path2

print(f'Las líneas en las que aparece la palabra {cad2} en {path2} son : {fun7(pathn2,cad2)}')

#----------------------------------------------------------------------------

print('\nPALABRAS ÚNICAS')
path3 = input('Introduzca la dirección del archivo : ')
pathn3:str = '../../' + path3

print(f'Las palabras únicas en {path3} son : {fun8(pathn3)}')

#----------------------------------------------------------------------------

print('\nLONGITUD PROMEDIO DE LÍNEAS')
path4 = input('Introduzca la dirección del archivo : ')
pathn4:str = '../../' + path4

print(f'La longitud promedio de las líneas en {path4} es de {fun9(pathn4)} palabras')
