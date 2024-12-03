from Entrega3.tipos.red_social import *

if __name__ == '__main__':
    raiz = '../'
    rrss = Red_social.parse(raiz+'usuarios.txt', raiz+'relaciones.txt', es_dirigido=False)
    
    print('Nº Predecesores de cada vértice')
    for i in rrss.vertices():
        print(f'{i} - {len(rrss.predecessors(i))}')
    
    print('\nNº Vecinos de cada vértice')
    for i in rrss.vertices():
        print(f'{i} - {len(rrss.successors(i))}')