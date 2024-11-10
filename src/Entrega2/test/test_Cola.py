from Entrega2.tipos.Cola import Cola

print('TEST DE COLA\n\n----------------------------------------')

cola = Cola()
ls:list = ['perro','loro','gato','hamster','conejo']
cola.add_all(ls)
print(f'\nCreamos una cola a la que se le agregan los siguientes elementos : {ls}\n\nResultado de la cola : ListaOrdenada({cola})')

print('\n----------------------------------------')

elim = cola.remove_all()
print(f'\nLos elementos eliminados al utilizar remove_all() son : {elim}')
cola.add_all(elim)

print('\n----------------------------------------')

e1:str = 'cobaya'
e2:str = 'serpiente'
e3:str = 'araña'
print('\nComprobamos si se añaden elementos de forma correcta :')
cola.add(e1)
print(f'\nLista despues de añadirle {e1} : {cola}')
cola.add(e2)
print(f'\nLista despues de añadirle {e2} : {cola}')
cola.add(e3)
print(f'\nLista despues de añadirle {e3} : {cola}')