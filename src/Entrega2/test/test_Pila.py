from Entrega2.tipos.Pila import Pila

pila = Pila()
ls:list = ['perro','loro','gato','hamster','conejo']
pila.add_all(ls)
print(f'\nCreamos una pila a la que se le agregan los siguientes elementos : {ls}\n\nResultado de la pila : pila({pila})')

print('\n----------------------------------------')

elim = pila.remove()
print(f'\nEl elemento eliminado al utilizar remove() es : {elim}')
pila.add(elim)

print('\n----------------------------------------')

e1:str = 'cobaya'
e2:str = 'serpiente'
e3:str = 'araña'
print('\nComprobamos si se añaden elementos de forma correcta :')
pila.add(e1)
print(f'\nLista despues de añadirle {e1} : {pila}')
pila.add(e2)
print(f'\nLista despues de añadirle {e2} : {pila}')
pila.add(e3)
print(f'\nLista despues de añadirle {e3} : {pila}')