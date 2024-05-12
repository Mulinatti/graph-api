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
            if adjacencias[i][i] > 0:
                incidencia[i][indice_aresta] = 0
                indice_aresta += 1
            
            for j in range(self.num_vertices):
                if adjacencias[i][j] > 0 and i != j:
                    for _ in range(adjacencias[i][j]):
                        incidencia[i][indice_aresta] = 1
                        incidencia[j][indice_aresta] = -1
                        indice_aresta += 1
        
        return incidencia
    
    def contar_arestas(self, adjacencias: List[List[int]]):
        num_arestas = 0
        for i in range(len(adjacencias)):
            for j in range(i, len(adjacencias)):
                if i <= j:  
                    num_arestas += abs(adjacencias[i][j])
        return num_arestas   
    
    def contar_vertices(self, mat_adj: List[List[int]]) -> int:
        return len(mat_adj)
    
    def calcular_graus(self, adjacencias: List[List[int]]):
        soma_graus = []
        # Para armazenar os graus de entrada totais
        total_entrada = []
        # Para armazenar os graus de saída totais
        total_saida = []
        # Para armazenar temporariamente os valores de entrada e saída
        # antes deles serem anexados aos totais
        entrada, saida = 0, 0
        for i in range(len(adjacencias)):
            # Para impedir a lista de ir out of bounds
            if i >= len(adjacencias[i]):
                break
            for j in range(len(adjacencias)):
                # Adicionando os valores negativos na variável entrada e os potivos na variável saida
                if adjacencias[j][i] < 0:
                    entrada += adjacencias[j][i]
                else:
                    saida += adjacencias[j][i]
            total_entrada.append(entrada)
            total_saida.append(saida)
            # Reiniciando os valores auxiliares antes da próxima iteração
            entrada, saida = 0, 0
        for i in range(len(total_entrada)):
            # Calculando o Grau total da vértice
            total = total_entrada[i] + total_saida[i]
            # Iterando o objeto Vertice usando os valores adquiridos previamente
            nome = Vertice(total_entrada[i], total_saida[i], total)
            # Adicionando o objeto a lista
            soma_graus.append(nome)
        return soma_graus
