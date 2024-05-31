import unittest

from collections import deque

def verifica_grafo_bipartido(adjacente, digrafo: bool, valorado: bool):
    n = len(adjacente)
    cor = [-1] * n  # -1 significa não colorido, 0 e 1 serão as duas cores

    def bfs(v):
        fila = deque([v])
        cor[v] = 0  # Inicializa com a cor 0

        while fila:
            u = fila.popleft()

            for j in range(n):
                if digrafo:
                    if adjacente[u][j] > 0 or (valorado and adjacente[u][j] is not None):
                        if cor[j] == -1:
                            cor[j] = 1 - cor[u]
                            fila.append(j)
                        elif cor[j] == cor[u]:
                            return False
                else:
                    if adjacente[u][j] > 0 or (valorado and adjacente[u][j] is not None):
                        if cor[j] == -1:
                            cor[j] = 1 - cor[u]
                            fila.append(j)
                        elif cor[j] == cor[u]:
                            return False
        return True

    for vertice in range(n):
        if cor[vertice] == -1:
            if not bfs(vertice):
                return False
    return True

class TestVerificaGrafoBipartido(unittest.TestCase):

    def test_grafo_nao_direcionado_bipartido(self):
        adjacente = [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        self.assertTrue(verifica_grafo_bipartido(adjacente, digrafo=False, valorado=False))

    def test_grafo_nao_direcionado_nao_bipartido(self):
        adjacente = [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        self.assertFalse(verifica_grafo_bipartido(adjacente, digrafo=False, valorado=False))

    def test_digrafo_bipartido(self):
        adjacente = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0]
        ]
        self.assertTrue(verifica_grafo_bipartido(adjacente, digrafo=True, valorado=False))

    def test_digrafo_nao_bipartido(self):
        adjacente = [
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0]
        ]
        self.assertTrue(verifica_grafo_bipartido(adjacente, digrafo=True, valorado=False))

    def test_grafo_valorado_bipartido(self):
        adjacente = [
            [0, 3, None, 2],
            [3, 0, 4, None],
            [None, 4, 0, 1],
            [2, None, 1, 0]
        ]
        self.assertFalse(verifica_grafo_bipartido(adjacente, digrafo=False, valorado=True))

    def test_grafo_valorado_nao_bipartido(self):
        adjacente = [
            [0, 3, 4, 2],
            [3, 0, 4, None],
            [4, 4, 0, 1],
            [2, None, 1, 0]
        ]
        self.assertFalse(verifica_grafo_bipartido(adjacente, digrafo=False, valorado=True))

    def test_digrafo_valorado_bipartido(self):
        adjacente = [
            [0, 3, None, None],
            [None, 0, 4, None],
            [None, None, 0, 1],
            [2, None, None, 0]
        ]
        self.assertFalse(verifica_grafo_bipartido(adjacente, digrafo=True, valorado=True))

    def test_digrafo_valorado_nao_bipartido(self):
        adjacente = [
            [0, 3, None, 2],
            [None, 0, 4, None],
            [None, None, 0, 1],
            [2, None, None, 0]
        ]
        self.assertFalse(verifica_grafo_bipartido(adjacente, digrafo=True, valorado=True))

if __name__ == '__main__':
    unittest.main()

