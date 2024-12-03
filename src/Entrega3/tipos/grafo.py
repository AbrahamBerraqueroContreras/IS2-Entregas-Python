from __future__ import annotations

from typing import TypeVar, Generic, Dict, Set, Optional, Callable
import matplotlib.pyplot as plt
import networkx as nx

V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas

class Grafo(Generic[V, E]):
    def __init__(self, es_dirigido: bool = True, adyacencias: Dict[V, Dict[V, E]] = {}):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = adyacencias
    
    @staticmethod
    def of(es_dirigido: bool = True, adyacencias: Dict[V, Dict[V, E]] = {}) -> Grafo[V, E]:
        return Grafo(es_dirigido, adyacencias)
    
    def add_vertex(self, vertice: V) -> None:
        self.adyacencias[vertice] = {}

    def add_edge(self, origen: V, destino: V, arista: E) -> None:
        self.adyacencias[origen] |= {destino:arista}
        self.adyacencias[destino] |= {} if self.es_dirigido else {origen:arista}
    
    def successors(self, vertice: V) -> Set[V]:
        return set(self.adyacencias[vertice].keys())

    def predecessors(self, vertice: V) -> Set[V]:
        return set(i for i in self.adyacencias if vertice in self.adyacencias[i].keys())

    def edge_weight(self, origen: V, destino: V) -> Optional[E]:
        return self.adyacencias[origen][destino] if self.edge_exists(origen,destino) else None

    def vertices(self) -> Set[V]:
        return set(self.adyacencias.keys())
    
    def edge_exists(self, origen: V, destino: V) -> bool:
        return destino in self.adyacencias[origen].keys()

    def subgraph(self, vertices: Set[V]) -> Grafo[V, E]:
        '''
        :Funcionamiento
        Recorre el grafo buscando un vertice (i) perteneciente al conjunto de vertices dado y añade 
        dicho vertice en el nuevo grafo con las conexiones con vertices que tambien se encuentren 
        en el conjunto vertices.
        
        :Forma_clásica
        dict1 = {}
        for i in self.adyacencias:
            if i in vertices:
                dict2 = {}
                for j in self.adyacencias[i]:
                    if j in vertices:
                        dict2 |= {j:self.adyacencias[j][i]}
                dict1 |= {i:dict2}
        return dict1
        '''
        
        return Grafo.of(es_dirigido=self.es_dirigido,adyacencias={i:{j:self.adyacencias[i][j] for j in self.adyacencias[i] if j in vertices} for i in self.adyacencias if i in vertices})

    def inverse_graph(self) -> Grafo[V, E]:
        if self.es_dirigido:
            '''
            :Funcionamiento
            Toma los vértices del grafo (i) y rellena sus conexiones con otros vértices si el primer 
            vertice se encuentra en el dicionario de conexiones del segundo (if i in self.adyacencias[j].keys()), 
            es decir, tomar el vertice de la conexion a la que pertenecía (j) y el peso de la 
            arista que forman (self.adyacencias[j][i]).
            
            :Forma_clásica
            dict1 = {}
            for i in self.adyacencias:
                dict2 = {}
                for j in self.adyacencias:
                    if i in self.adyacencias[j].keys():
                        dict2 |= {j:self.adyacencias[j][i]}
                dict1 |= {i:dict2}
            return dict1
            '''
            return Grafo.of(es_dirigido=True,adyacencias={i:{j:self.adyacencias[j][i] for j in self.adyacencias if i in self.adyacencias[j].keys()} for i in self.adyacencias})
        else:
            raise ValueError('El grafo no es dirigido')
        

    def draw(self, titulo: str = "Grafo", 
            lambda_vertice: Callable[[V], str] = str, 
            lambda_arista: Callable[[E], str] = str) -> None:
        
        # Crear un grafo de NetworkX
        G = nx.DiGraph() if self.es_dirigido else nx.Graph()
    
        # Añadir nodos y aristas
        for vertice in self.vertices():
            G.add_node(vertice, label=lambda_vertice(vertice))  # Usamos lambda_vertice para personalizar el nodo
        for origen in self.vertices():
            for destino, arista in self.adyacencias[origen].items():
                G.add_edge(origen, destino, label=lambda_arista(arista))  # Usamos lambda_arista para personalizar la arista
    
        # Dibujar el grafo
        pos = nx.spring_layout(G)  # Distribución de los nodos
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=500, 
                labels=nx.get_node_attributes(G, 'label'))  # Usamos las etiquetas personalizadas de los vértices
    
        # Dibujar las etiquetas de las aristas (con la representación personalizada)
        edge_labels = nx.get_edge_attributes(G, "label")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
        plt.title(titulo)
        plt.show()

        
    def __str__(self) -> str:
        '''
        :Forma_clásica
        ls1:list = []
        for i in self.adyacencias :
            ls2:list = []
            for j in self.adyacencias[i] :
                ls2.append(f'{j} ({self.adyacencias[i][j]})')
            ls1.append(f'{i} -> ' + ', '.join(ls2))
        return '\n'.join(ls1)
        '''
        return '\n'.join([f'{i} -> ' + ', '.join([f'{j} ({self.adyacencias[i][j]})' for j in self.adyacencias[i]]) for i in self.adyacencias])

if __name__ == '__main__':
    # Crear un grafo dirigido
    grafo = Grafo.of(es_dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_edge("A", "B", 5)
    grafo.add_edge("A", "C", 7)
    grafo.add_edge("B", "C", 3)
    print(grafo)
    print(grafo.subgraph({'A','B'}))
    print(grafo.inverse_graph())
    
    # Dibujar el grafo
    #grafo.draw(titulo="Mi Grafo Dirigido")
    #grafo.inverse_graph().draw(titulo="Inverso del Grafo Dirigido")
    
    # editado : self.of -> Grafo.of