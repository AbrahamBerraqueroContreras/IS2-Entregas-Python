from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod
from Examen2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')

class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad:int):
        self._elements = []
        self._capacidad = capacidad
        
    @classmethod
    def of(cls, capacidad:int) -> int:
        return cls(capacidad)
        print(True)
    
    def is_full(self) -> bool:
        if self._capacidad == 0:
            return True
        return False
        
    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena.")
        self._elements.append(e)
        self._capacidad -= 1