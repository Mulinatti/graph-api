from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

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


class Grafo(GrafoAbstrato):
    """Classe que encapsula todos os dados necessários de um grafo.
       Possui as matrizes de adjacências e de incidência, o número
       de vértices e de arestas, e uma lista com o grau de cada
       vértice."""
    def __init__(self, mat_adj: List[List[int]]):
        super().__init__(mat_adj)
        self.lista_de_graus = self.calcular_graus(mat_adj)
    
    def adj_para_incid(self, adjacencias) -> List[List[int]]:
        # Populando a nova matriz com zeros
        incidencia = []
        for _ in range(self.num_vertices):
            incidencia.append([0] * self.num_arestas)
        
        indice_aresta = 0
        for i in range(self.num_vertices):
            # Laços
            if adjacencias[i][i] != 0:
                incidencia[i][indice_aresta] += adjacencias[i][i]
                indice_aresta += 1
            
            for j in range(i+1, self.num_vertices):
                if adjacencias[j][i] != 0:
                    incidencia[i][indice_aresta] += adjacencias[j][i]
                    incidencia[j][indice_aresta] += adjacencias[j][i]
                    indice_aresta += 1
        return incidencia

    def contar_arestas(self, adjacencias: List[List[int]]) -> int:
        pass

    def calcular_graus(self, adjacencias: List[List[int]]) -> List[int]:
        pass


@dataclass
class Vertice:
    """Classe de dados necessária para armazenar
       os graus de entrada e de saída de um vértice."""
    grau_entrada: int
    grau_saida: int
    grau_total: int


class Digrafo(GrafoAbstrato):
    """Classe que encapsula os dados necessário para modelar
       um grafo direcionado, e possui uma lista de vértices,
       que armazenam seus graus."""
    def __init__(self, mat_adj: List[List[int]]):
        super().__init__(mat_adj)
        self.lista_de_graus = self.calcular_graus(mat_adj)
    
    def adj_para_incid(self, adjacencias: List[List[int]]):
        # Zerando a matriz de incidência.
        incidencia = []
        incidencia = [[0] * self.num_arestas for _ in range(self.num_vertices)]
        
        indice_aresta = 0
        for i in range(self.num_vertices):
            for j in range(i+1, self.num_vertices):
                if adjacencias[i][j] != 0:
                    incidencia[i][indice_aresta] += adjacencias[i][j]
                    incidencia[j][indice_aresta] -= adjacencias[i][j]
                    indice_aresta += 1
        
        return incidencia
    
    def calcular_graus(self, adjacencias: List[List[int]]):
        pass
