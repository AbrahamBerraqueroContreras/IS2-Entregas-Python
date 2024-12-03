from typing import TypeVar, List, Set, Optional
from Entrega3.tipos.grafo import Grafo
from Entrega2.tipos.Cola import Cola
from Entrega2.tipos.Pila import Pila

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    visitados:Set = set()
    cola = Cola()
    
    cola.add(inicio)
    predecesores:dict = {inicio:None}
    
    while not cola.is_empty():
        vertice = cola.remove()
        
        if vertice == destino:
            break
        
        if vertice not in visitados:
            visitados.add(vertice)
            
            for vecino in grafo.successors(vertice):
                if vecino not in visitados:
                    cola.add(vecino)
                    predecesores[vecino] = vertice

    return reconstruir_camino(predecesores, destino)

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    visitados:Set = set()
    pila = Pila()
    pila.add(inicio)
    predecesores = {inicio:None}
    
    while not pila.is_empty():
        vertice = pila.remove()
        
        if vertice == destino:
            break
        
        if vertice not in visitados:
            visitados.add(vertice)
            
            for vecino in grafo.successors(vertice):
                if vecino not in visitados:
                    pila.add(vecino)
                    predecesores[vecino] = vertice
    return reconstruir_camino(predecesores, destino)

def reconstruir_camino(predecesores: dict, destino: V) -> List[V]:
    camino:list = []
    vertice_actual:V = destino
    
    while vertice_actual in predecesores:
        camino.insert(0, vertice_actual)
        vertice_actual = predecesores[vertice_actual]
    return camino

if __name__ == '__main__':
    print(reconstruir_camino({'A':None,'B':'A','C':'B','D':'C'}, 'D'))
    
    grafo = Grafo.of(True,{'A':{'B':None,'C':None},'B':{'D':None,'E':None},'C':{'F':None,'G':None},'D':{},'E':{},'F':{},'G':{}})
    print(bfs(grafo,'C','E'))
    print(dfs(grafo,'C','E'))
    grafo.draw()