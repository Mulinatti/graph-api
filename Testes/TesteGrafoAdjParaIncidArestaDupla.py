from Classes.Grafo import Grafo
import unittest

class TesteGrafoAdjParaIncidArestaDupla(unittest.testCase):
    @classmethod
    def setUpClass(self):
        self.matriz1 = [
            [0, 2, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0]
        ]
        self.resultado1 = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1]
        ]

        self.matriz2 = [
            [0, 2, 2],
            [2, 0, 2],
            [2, 2, 0]
        ]
        self.resultado2 = [
            [1, 1, 1, 1, 0, 0],
            [1, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 1, 1]
        ]
    
    def test_matriz1(self):
        self.g = Grafo(self.matriz1, False)
        self.assertEqual(self.g.mat_incid, self.resultado1)
    
    def test_matriz2(self):
        self.g = Grafo(self.matriz2, False)
        self.assertEqual(self.g.mat_incid, self.resultado2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
