from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod
from Entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')

class Pila(Agregado_lineal[E]):
    def __init__(self):
        self._elements:Pila[E] = []
        
    @classmethod
    def of(cls) -> Pila[E]:
        return cls(Pila[E])
        
    def add(self, e: E) -> None:
        self._elements.insert(0,e)