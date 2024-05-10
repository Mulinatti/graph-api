class Grafo:
    """Classe que encapsula todos os dados necessários de um grafo.
       Possui as matrizes de adjacências e de incidência, o número
       de vértices e de arestas, e uma lista com o grau de cada
       vértice."""
    def __init__(self, mat_adj: list[list[int]]):
        self.mat_adj        = mat_adj
        self.mat_incid      = self.adj_para_incid(mat_adj)
        self.num_vertices   = len(mat_adj)
        self.num_arestas    = self.contar_arestas(mat_adj)
        self.lista_de_graus = self.calcular_grau(mat_adj)
    
    def adj_para_incid(self, adjacencias) -> list[list[int]]:
        pass

    def contar_arestas(self, m_adjacencias: list[list[int]]) -> int:
        pass

    def calcular_grau(self, m_adjacencias: list[list[int]]) -> list[int]:
        pass

