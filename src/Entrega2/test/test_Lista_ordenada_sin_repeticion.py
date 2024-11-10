from Entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion
import inspect

print('TEST DE LISTA ORDENADA SIN REPETICIÓN\n\n----------------------------------------')

ord = lambda x : x
listaOrdenadaSinRep = Lista_ordenada_sin_repeticion(ord)
print(f'\nCreamos una lista con criterio de clasificación {inspect.getsource(ord)}')

ls:list = [8,-22,50,12,43,-4,22,12,11,11]
listaOrdenadaSinRep.add_all(ls)
print(f'Introducimos los siguientes elementos en el mismo orden : {ls}\n\nResultado de la lista : listaOrdenadaSinRep({listaOrdenadaSinRep})')

print('\n----------------------------------------')

elim = listaOrdenadaSinRep.remove()
print(f'\nEl elemento eliminado al utilizar remove() es : {elim}')
listaOrdenadaSinRep.add(elim)

print('\n----------------------------------------')

elim = listaOrdenadaSinRep.remove_all()
print(f'\nLos elementos eliminados al utilizar remove_all() son : {elim}')
listaOrdenadaSinRep.add_all(elim)

print('\n----------------------------------------')

num1:int = -31
num2:int = 96
num3:int = 22
print('\nComprobamos si se añaden elementos de forma correcta :')
listaOrdenadaSinRep.add(num1)
print(f'\nLista despues de añadirle el número {num1} : {listaOrdenadaSinRep}')
listaOrdenadaSinRep.add(num2)
print(f'\nLista despues de añadirle el número {num2} : {listaOrdenadaSinRep}')
listaOrdenadaSinRep.add(num3)
print(f'\nLista despues de añadirle el número {num3} : {listaOrdenadaSinRep}')
