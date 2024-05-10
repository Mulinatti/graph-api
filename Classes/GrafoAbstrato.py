from abc import ABC, abstractmethod # para disponibilizar classes abstratas
from typing import List             # para disponibilizar List para anotações de tipo

class GrafoAbstrato(ABC):
    """Classe abstrata com todas as funcionalidades comuns aos
       dois tipos de grafos modelados: grafo e digrafo (grafo
       dirigido)"""
    def __init__(self, mat_adj: List[List[int]]):
        self.mat_adj = mat_adj
        self.num_vertices = len(mat_adj)
        self.num_arestas = self.contar_arestas(mat_adj)
        self.mat_incid = self.adj_para_incid(mat_adj)
    
    @abstractmethod
    def contar_arestas(self, adjacencias: List[List[int]]):
        pass

    @abstractmethod
    def adj_para_incid(self, adjacencias: List[List[int]]):
        pass
