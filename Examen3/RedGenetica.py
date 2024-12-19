from __future__ import annotations

from typing import Dict
from Entrega3.tipos.grafo import Grafo
from Entrega3.tipos.recorridos import *
from Examen3.gen import Gen
from Examen3.RelacionGenAGen import RelacionGenAGen

class RedGenetica(Grafo[Gen, RelacionGenAGen]):
    
    def __init__(self, es_dirigido: bool = False, adyacencias: Dict[V, Dict[V, E]] = {}) -> None:
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of(es_dirigido: bool = False, adyacencias: Dict[V, Dict[V, E]] = {}) -> RedGenetica:
        return RedGenetica(es_dirigido,adyacencias)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> RedGenetica:
        rs = RedGenetica.of(es_dirigido=es_dirigido)
        
        for line in open(f1):
            ls = line.strip('\n').split(',')
            rs.genes_por_nombre |= {ls[0]:Gen.of(ls[0],ls[1],int(ls[2]),ls[3])}
            rs.add_vertex(Gen.of(ls[0],ls[1],int(ls[2]),ls[3]))
        
        for line in open(f2):
            ls = line.strip('\n').split(',')
            rs.add_edge(rs.genes_por_nombre[ls[0]],rs.genes_por_nombre[ls[1]],RelacionGenAGen.of(ls[0],ls[1],float(ls[2])))
        
        return rs