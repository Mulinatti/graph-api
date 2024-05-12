from typing import List

def contar_arestas(adjacencias: List[List[int]]) -> int:
        num_arestas = 0
        for i in range(len(adjacencias)):
            for j in range(i, len(adjacencias)):
                if i <= j:
                    num_arestas += adjacencias[i][j]
        return num_arestas
