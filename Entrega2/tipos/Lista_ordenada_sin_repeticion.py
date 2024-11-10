from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod
from Entrega2.tipos.Agregado_lineal import Agregado_lineal
from Entrega2.tipos.Lista_ordenada import Lista_ordenada

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada_sin_repeticion(Lista_ordenada[E, R], Generic[E, R]):
    def add(self, e: E) -> None:
        if e not in self._elements:
            super().add(e)