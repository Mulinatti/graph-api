from Classes.GrafoAbstrato import GrafoAbstrato
from typing import List # para disponibilizar List para anotações de tipo

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
        soma_graus = []
        # Para armazenar temporariamente o valor do grau durante as iterações
        aux = 0
        for i in range(len(adjacencias)):
            # Para impedir que a lista dê out of bounds.
            if i >= len(adjacencias[i]):
                break
            for j in range(len(adjacencias)):
                # Para pegar os valores verticalmente, ao invês de horizontalmente
                aux += adjacencias[j][i]
            # Adicionando o valor a lista
            soma_graus.append(aux)
            # Zerando o valor auxiliar antes da próxima iteração
            aux = 0
        return soma_graus

