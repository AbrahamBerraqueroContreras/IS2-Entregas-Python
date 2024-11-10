from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod
from Entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order
    
    @classmethod
    def of(cls, order: Callable[[E], R]) -> Lista_ordenada[E, R]:
        return cls(order)

    def __index_order(self, e: E) -> int:
        for i in range(self.size()):
            '''
            Se utiliza el self.order() en ambos terminos para invertir los signos en caso de orden decreciente
            Ejemplo : 2 < 3 --(lambda x : -x)--> -2 <-3 
            '''
            if (self._order(e) < self._order(self._elements[i])):
                return i
        '''
        En el caso en el que no se ejecute return i (es decir al ser mayor que el resto de la lista),
        el método retorna el último término (correspondiente a len(self._elements))
        '''
        return len(self._elements)
    
    def add(self, e: E) -> None:
        i = self.__index_order(e)    
        self._elements.insert(i,e)