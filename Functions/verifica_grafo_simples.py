import unittest

def verifica_grafo_simples(adjacencias, digrafo: bool, valorado: bool):
    vertices = len(adjacencias)
    
    # Verifica se a matriz de adjacências é quadrada
    if any(len(row) != vertices for row in adjacencias):
        raise ValueError("A matriz de adjacências deve ser quadrada.")
    
    for i in range(vertices):
        # Verifica se há laços
        if adjacencias[i][i] != 0:
            return False
        
        for j in range(vertices):
            if digrafo:
                # Em grafos direcionados, verifica se há múltiplas arestas na mesma direção
                if not valorado and adjacencias[i][j] > 1:
                    return False
            else:
                # Em grafos não direcionados, verifica se há múltiplas arestas
                if not valorado and adjacencias[i][j] > 1:
                    return False
                if j > i and adjacencias[i][j] != adjacencias[j][i]:
                    return False
    
    return True


class TestGrafo(unittest.TestCase):
    def test_verificar_simples(self):
        # Caso de teste para grafo simples não direcionado e não valorado
        adjacencias_nd_nv = [
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0]
        ]
        self.assertTrue(verifica_grafo_simples(adjacencias_nd_nv, digrafo=False, valorado=False))

        # Caso de teste para grafo não simples não direcionado e não valorado
        adjacencias_nd_nv_nao_simples = [
            [0, 2, 0, 0],
            [2, 0, 2, 0],
            [0, 2, 0, 2],
            [0, 0, 2, 0]
        ]
        self.assertFalse(verifica_grafo_simples(adjacencias_nd_nv_nao_simples, digrafo=False, valorado=False))

        # Caso de teste para grafo simples direcionado e não valorado
        adjacencias_d_nv = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]
        ]
        self.assertTrue(verifica_grafo_simples(adjacencias_d_nv, digrafo=True, valorado=False))
    
        # Caso de teste para grafo valorado (devemos decidir a política para grafos valorados)
        adjacencias_valorado = [
            [0, 3, 0, 0],
            [3, 0, 2, 0],
            [0, 2, 0, 4],
            [0, 0, 4, 0]
        ]
        # Se o grafo é valorado, ignoramos as múltiplas arestas
        self.assertTrue(verifica_grafo_simples(adjacencias_valorado, digrafo=False, valorado=True))
    
        # Caso de teste para grafo não quadrado deve lançar exceção
        adjacencias_nao_quadrado = [
            [0, 1, 0],
            [1, 0, 1]
        ]
        with self.assertRaises(ValueError):
            verifica_grafo_simples(adjacencias_nao_quadrado, digrafo=False, valorado=False)

if __name__ == '__main__':
    unittest.main()
