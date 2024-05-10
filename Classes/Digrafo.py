from GrafoAbstrato import GrafoAbstrato
from typing import List      # para disponibilizar List para anotações de tipo
from Vertice import Vertice

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
    
    def contar_arestas(self, adjacencias: List[List[int]]):
        pass
    
    def calcular_graus(self, adjacencias: List[List[int]]):
        pass
