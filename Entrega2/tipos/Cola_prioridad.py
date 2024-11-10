from __future__ import annotations
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod

E = TypeVar('E')
P = TypeVar('P')

class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements:List[E] = []
        self._priorities:List[E] = []
        
    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return self.size() == 0
    
    def elements(self) -> List[E]:
        return self._elements.copy()

    def __index_order(self, priority: P) -> int:
        for i in range(self.size()) :
            if priority < self._priorities[i]:
                return i
        return len(self._elements)

    def add(self, e: E, priority: P) -> None:
        i = self.__index_order(priority)
        self._elements.insert(i,e)
        self._priorities.insert(i,priority)
        
    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for e,priority in ls :
            self.add(e,priority)

    def remove(self) -> E:
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        self._priorities.pop(0)
        return self._elements.pop(0)
    
    def remove_all(self) -> List[E]:
        removed_elements = self._elements.copy()
        self._elements.clear()
        self._priorities.clear()
        return removed_elements
    
    def decrease_priority(self, e: E, new_priority: P) -> None:
        for i in range(self.size()):
            if e == self._elements[i]:
                self._elements.pop(i)
                self._priorities.pop(i)
                break
        self.add(e,new_priority)
    
    def __str__(self):
        return f'{self._elements}'