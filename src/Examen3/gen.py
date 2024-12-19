from __future__ import annotations

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Gen:
    nombre: str 
    tipo: str 
    num_mutaciones: int
    loc_cromosoma: str
    
    @staticmethod
    def of(nombre:str,tipo:str,num_mutaciones:int,loc_cromosoma:str) -> Gen:
        return Gen(nombre,tipo,num_mutaciones,loc_cromosoma)
    
    @staticmethod
    def parse(fichero:str) -> List[Gen]:
        ls_gen:list[Gen] = []
        
        for line in open(fichero) :
            ls = line.strip().split(',')
            ls_gen.append(Gen(ls[0],ls[1],int(ls[2]),ls[3]))
        
        return ls_gen

if __name__ == '__main__':
    gen = Gen.of('TP53','supresor tumoral',256,'17p13.1')
    print(gen)
    print(Gen.parse('genes.txt'))