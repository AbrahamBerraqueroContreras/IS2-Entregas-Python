from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod
from Entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')

class Cola(Agregado_lineal[E]):
    def __init__(self):
        self._elements:Cola[E] = []
        
    @classmethod
    def of(cls) -> Cola[E]:
        return cls(Cola[E])
        
    def add(self, e: E) -> None:
        self._elements.append(e)