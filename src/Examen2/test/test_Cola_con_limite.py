from Examen2.tipos.Cola_con_limite import ColaConLimite

print('TESTs COLA CON LÍMITE Y AGREGADO LINEAL')

print('\nDeclaro una variable de tipo ColaConLimite y le impongo un límite de 4 elementos')
cola = ColaConLimite.of(4)

e1:str = 'pez'
e2:str = 'perro'
e3:str = 'serpiente'
e4:str = 'mono'

print(f'\nLe agrego los elementos {e1}, {e2}, {e3}, {24}')
cola.add(e1)
cola.add(e2)
cola.add(e3)
cola.add(e4)

e5:str = 'gato'
print(f'\nTrato de añadirle un nuevo elemento {e5}')
try:
    cola.add(e5) # Debe lanzar OverflowError
except OverflowError as e:
    print(e) # Debe imprimir: "La cola está llena."
    print(cola.remove()) # Debe imprimir: 'Tarea 1'