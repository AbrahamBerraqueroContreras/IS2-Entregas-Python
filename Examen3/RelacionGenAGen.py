from __future__ import annotations

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str 
    nombre_gen2: str 
    conexion: float
    
    @staticmethod
    def of(nombre_gen1:str,nombre_gen2:str,conexion:float) -> RelacionGenAGen:
        assert abs(conexion)<1, 'Conexión no-válida'
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)
    
    @staticmethod
    def parse(fichero:str) -> List[RelacionGenAGen]:
        ls_relacion:list[RelacionGenAGen] = []
        
        for line in open(fichero) :
            ls = line.strip().split(',')
            ls_relacion.append(RelacionGenAGen(ls[0],ls[1],int(ls[2])))
        
        return ls_relacion