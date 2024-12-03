from __future__ import annotations

from dataclasses import dataclass
from typing import Dict
from datetime import date, datetime
from Entrega3.tipos.grafo import *
from Entrega3.tipos.recorridos import *

@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        return Usuario(dni,nombre,apellidos,fecha_nacimiento)
    
    def __str__(self) -> str:
        return f'{self.dni} - {self.nombre}'

@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0 # Contador de relaciones. Servirá para asignar identificadores únicos a las relaciones.
    
    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        Relacion.__n += 1
        return Relacion(Relacion.__n,interacciones,dias_activa)
    
    def __str__(self) -> str:
        return f'{self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones}'

class Red_social(Grafo[Usuario, Relacion]):
    def __init__(self, es_dirigido: bool = False, adyacencias: Dict[V, Dict[V, E]] = {}) -> None:
        super().__init__(es_dirigido)
        '''
        usuarios_dni: Diccionario que asocia un DNI de usuario con un objeto Usuario.
        Va a ser útil en la lectura del fichero de relaciones para poder acceder a los usuarios
        '''
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False, adyacencias: Dict[V, Dict[V, E]] = {}) -> Red_social:
        return Red_social(es_dirigido,adyacencias)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> Red_social:
        """
        Método de factoría para crear una Red Social desde archivos de usuarios y relaciones.
        
        :param f1: Archivo de usuarios.
        :param f2: Archivo de relaciones.
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        rs = Red_social.of(es_dirigido=es_dirigido)
        
        for line in open(f1):
            ls = line.strip('\n').split(',')
            rs.usuarios_dni |= {ls[0]:Usuario.of(ls[0],ls[1],ls[2],ls[3])}
            rs.add_vertex(Usuario.of(ls[0],ls[1],ls[2],ls[3]))
        
        for line in open(f2):
            ls = line.strip('\n').split(',')
            rs.add_edge(rs.usuarios_dni[ls[0]],rs.usuarios_dni[ls[1]],Relacion.of(ls[2],ls[3]))
        
        return rs
    
if __name__ == '__main__':
    raiz = '../'
    rrss = Red_social.parse(raiz+'usuarios.txt', raiz+'relaciones.txt', es_dirigido=False)
    

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    camino = bfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'])
    g_camino = rrss.subgraph(camino)
    
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: e.id)
    
    '''
    :Error : g_camino = rrss
    :Problema : Al crear el subgrafo g_camino del grafo rrss, la función subgraph añadía (y no sustituía) los
    vertices de g_camino al grafo rrss y devolvía el grafo self (rrss), por lo que g_camino = rrss.
    :Solución : Cambiar el self.of() por Grafo.of() de la función subgraph, de modo que se crea
    una instancia de grafo vacía y pueden añadirse los vértices de g_camino sin problema.
    '''