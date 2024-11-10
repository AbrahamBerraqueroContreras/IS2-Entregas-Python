from Entrega2.tipos.Lista_ordenada import Lista_ordenada
import inspect

print('TEST DE LISTA ORDENADA\n\n----------------------------------------')

ord = lambda x : -x
listaOrdenada = Lista_ordenada(ord)
print(f'\nCreamos una lista con criterio de clasificación {inspect.getsource(ord)}')

ls:list = [2,8,5,1,9,5]
listaOrdenada.add_all(ls)
print(f'Introducimos los siguientes elementos en el mismo orden : {ls}\n\nResultado de la lista : ListaOrdenada({listaOrdenada})')

print('\n----------------------------------------')

elim = listaOrdenada.remove()
print(f'\nEl elemento eliminado al utilizar remove() es : {elim}')
listaOrdenada.add(elim)

print('\n----------------------------------------')

elim = listaOrdenada.remove_all()
print(f'\nLos elementos eliminados al utilizar remove_all() son : {elim}')
listaOrdenada.add_all(elim)

print('\n----------------------------------------')

num1:int = -1
num2:int = 12
num3:int = 6
print('\nComprobamos si se añaden elementos de forma correcta :')
listaOrdenada.add(num1)
print(f'\nLista despues de añadirle el número {num1} : {listaOrdenada}')
listaOrdenada.add(num2)
print(f'\nLista despues de añadirle el número {num2} : {listaOrdenada}')
listaOrdenada.add(num3)
print(f'\nLista despues de añadirle el número {num3} : {listaOrdenada}')