import unittest

def depth_first_search(grafo, vertice, visitado):
    visitado[vertice] = True
    for i, val in enumerate(grafo[vertice]):
        if val != 0 and not visitado[i]:
            depth_first_search(grafo, i, visitado)

def grafo_conexo(grafo, digrafo=False, fracamente=False):
    n = len(grafo)
    
    # Verifica se a matriz de adjacências é quadrada
    if any(len(row) != n for row in grafo):
        raise ValueError("A matriz de adjacências deve ser quadrada.")
    
    # Verifica conectividade para grafos não direcionados
    if not digrafo:
        visitado = [False] * n
        depth_first_search(grafo, 0, visitado)
        return all(visitado)
    
    # Verifica conectividade forte para grafos direcionados
    def digrafo_forte_conexo(grafo):
        for start in range(n):
            visitado = [False] * n
            depth_first_search(grafo, start, visitado)
            if not all(visitado):
                return False
        return True
    
    # Verifica conectividade fraca para grafos direcionados
    def digrafo_fracamente_conexo(grafo):
        # Converte o grafo direcionado para um grafo não direcionado
        grafo_nao_direcionado = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grafo[i][j] != 0 or grafo[j][i] != 0:
                    grafo_nao_direcionado[i][j] = grafo_nao_direcionado[j][i] = 1
        
        # Verifica a conectividade do grafo não direcionado
        visitado = [False] * n
        depth_first_search(grafo_nao_direcionado, 0, visitado)
        return all(visitado)
    
    if fracamente:
        return digrafo_fracamente_conexo(grafo)
    else:
        return digrafo_forte_conexo(grafo)

class TestGrafoConexo(unittest.TestCase):
    def test_grafo_conexo_nao_direcionado(self):
        adjacencias_nd = [
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0]
        ]
        self.assertTrue(grafo_conexo(adjacencias_nd, digrafo=False))

    def test_grafo_conexo_nao_direcionado_desconexo(self):
        adjacencias_nd_desconexo = [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ]
        self.assertFalse(grafo_conexo(adjacencias_nd_desconexo, digrafo=False))

    def test_grafo_fortemente_conexo_direcionado(self):
        adjacencias_d = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0]
        ]
        self.assertTrue(grafo_conexo(adjacencias_d, digrafo=True))

    def test_grafo_fortemente_conexo_direcionado_desconexo(self):
        adjacencias_d_desconexo = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]
        ]
        self.assertFalse(grafo_conexo(adjacencias_d_desconexo, digrafo=True))
    
    def test_grafo_conexo_nao_direcionado_valorado(self):
        adjacencias_nd_valorado = [
            [0, 3, 0, 0],
            [3, 0, 2, 0],
            [0, 2, 0, 4],
            [0, 0, 4, 0]
        ]
        self.assertTrue(grafo_conexo(adjacencias_nd_valorado, digrafo=False))

    def test_grafo_conexo_direcionado_valorado(self):
        adjacencias_d_valorado = [
            [0, 3, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 4],
            [1, 0, 0, 0]
        ]
        self.assertTrue(grafo_conexo(adjacencias_d_valorado, digrafo=True))
    
    def test_grafo_fracamente_conexo_direcionado(self):
        adjacencias_d_fracamente_conexo = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ]
        self.assertTrue(grafo_conexo(adjacencias_d_fracamente_conexo, digrafo=True, fracamente=True))
    
    def test_grafo_fracamente_conexo_direcionado_desconexo(self):
        adjacencias_d_fracamente_conexo_desconexo = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]
        ]
        self.assertTrue(grafo_conexo(adjacencias_d_fracamente_conexo_desconexo, digrafo=True, fracamente=True))

if __name__ == '__main__':
    unittest.main()
