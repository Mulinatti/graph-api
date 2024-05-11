from Classes.Grafo import Grafo
import unittest

class TesteGrafoAdjParaIncidSimples(unittest.TestCase):
    """Classe para testar a função adj_para_incid() da classe Grafo (não sendo valorado)."""
    @classmethod
    def setUpClass(self):
        self.matriz1 = [
            [0, 1, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0]
        ]
        self.resultado1 = [
            [1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1]
        ]

        self.matriz2 = [
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0]
        ]
        self.resultado2 = [
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 1]
        ]
    
    def test_matriz1(self):
        self.g = Grafo(self.matriz1, False)
        self.assertEqual(self.g.mat_incid, self.resultado1)
    
    def test_matriz2(self):
        self.g = Grafo(self.matriz2, False)
        self.assertEqual(self.g.mat_incid, self.resultado2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
