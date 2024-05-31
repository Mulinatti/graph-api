import unittest

def verifica_grafo_regular(adjacente, digrafo: bool, valorado: bool):
    n = len(adjacente)  # número de nós

    # Verificar grafo não direcionado
    if not digrafo:
        graus = []
        for i in range(n):
            grau = 0
            for j in range(n):
                if valorado:
                    if adjacente[i][j] > 0:
                        grau += 1
                else:
                    grau += adjacente[i][j]
            graus.append(grau)
        
        primeiro_grau = graus[0]
        for grau in graus:
            if grau != primeiro_grau:
                return False
        return True

    # Verificar grafo direcionado
    else:
        graus_entrada = [0] * n
        graus_saida = [0] * n

        for i in range(n):
            for j in range(n):
                if valorado:
                    if adjacente[i][j] > 0:
                        graus_saida[i] += 1
                        graus_entrada[j] += 1
                else:
                    graus_saida[i] += adjacente[i][j]
                    graus_entrada[j] += adjacente[i][j]

        primeiro_grau_entrada = graus_entrada[0]
        primeiro_grau_saida = graus_saida[0]

        for grau_entrada, grau_saida in zip(graus_entrada, graus_saida):
            if grau_entrada != primeiro_grau_entrada or grau_saida != primeiro_grau_saida:
                return False
        return True

class TestVerificaGrafoRegular(unittest.TestCase):

    def test_grafo_nao_direcionado_regular(self):
        adjacente = [
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0]
        ]
        self.assertTrue(verifica_grafo_regular(adjacente, digrafo=False, valorado=False))

    def test_grafo_nao_direcionado_nao_regular(self):
        adjacente = [
            [0, 1, 0, 1],
            [1, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 1, 1, 0]
        ]
        self.assertFalse(verifica_grafo_regular(adjacente, digrafo=False, valorado=False))

    def test_digrafo_regular(self):
        adjacente = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
        self.assertTrue(verifica_grafo_regular(adjacente, digrafo=True, valorado=False))

    def test_digrafo_nao_regular(self):
        adjacente = [
            [0, 1, 0],
            [1, 0, 1],
            [1, 0, 0]
        ]
        self.assertFalse(verifica_grafo_regular(adjacente, digrafo=True, valorado=False))

    def test_grafo_valorado_regular(self):
        adjacente = [
            [0, 2, 3, 4],
            [2, 0, 1, 2],
            [3, 1, 0, 1],
            [4, 2, 1, 0]
        ]
        self.assertTrue(verifica_grafo_regular(adjacente, digrafo=False, valorado=True))

    def test_grafo_valorado_nao_regular(self):
        adjacente = [
            [0, 2, 3, 4],
            [2, 0, 1, 2],
            [3, 1, 0, 1],
            [4, 2, 1, 5]
        ]
        self.assertFalse(verifica_grafo_regular(adjacente, digrafo=False, valorado=True))

    def test_digrafo_valorado_regular(self):
        adjacente = [
            [0, 3, 2],
            [3, 0, 4],
            [2, 4, 0]
        ]
        self.assertTrue(verifica_grafo_regular(adjacente, digrafo=True, valorado=True))

    def test_digrafo_valorado_nao_regular(self):
        adjacente = [
            [0, 3, 2],
            [3, 0, 0],
            [2, 4, 0]
        ]
        self.assertFalse(verifica_grafo_regular(adjacente, digrafo=True, valorado=True))

if __name__ == '__main__':
    unittest.main()