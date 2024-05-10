from typing import List

class Grafo:
    """Classe que encapsula todos os dados necessários de um grafo.
       Possui as matrizes de adjacências e de incidência, o número
       de vértices e de arestas, e uma lista com o grau de cada
       vértice."""
    def __init__(self, mat_adj: List[List[int]], direcionado: bool):
        self.mat_adj        = mat_adj
        self.mat_incid      = self.adj_para_incid(mat_adj)
        self.num_vertices   = len(mat_adj)
        self.num_arestas    = self.contar_arestas(mat_adj)
        self.lista_de_graus = self.calcular_grau(mat_adj)
        self.direcionado    = direcionado
    
    def adj_para_incid(self, adjacencias) -> List[List[int]]:
        # Populando a nova matriz com zeros
        incidencia = []
        for _ in range(self.num_vertices):
            incidencia.append([0] * self.num_arestas)
        
        indice_aresta = 0
        # Algoritmo diferente dependendo de ser um grafo direcionado ou não.
        if self.direcionado:
            for i in range(self.num_vertices):
                for j in range(i+1, self.num_vertices):
                    if adjacencias[j][i] != 0:
                        incidencia[i][indice_aresta] += adjacencias[i][j]
                        incidencia[j][indice_aresta] += adjacencias[j][i]
                        indice_aresta += 1
            return incidencia
        
        # Não direcionado:
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

    def calcular_grau(self, adjacencias: List[List[int]]) -> List[int]:
        pass

