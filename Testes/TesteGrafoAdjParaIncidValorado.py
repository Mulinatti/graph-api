from Classes.Grafo import Grafo
import unittest

class TesteGrafoAdjParaIncidValorado(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.matriz1 = [
            [0, 20, 5],
            [20, 0, 15],
            [5, 15, 0]
        ]
        self.resultado1 = [
            [20, 5, 0],
            [20, 0, 15],
            [0, 5, 15]
        ]

        self.matriz2 = [
            [15, 3, 2],
            [3, 0, 0],
            [2, 0, 0]
        ]
        self.resultado2 = [
            [15, 3, 2],
            [0, 3, 0],
            [0, 0, 2]
        ]
    
    def test_matriz1(self):
        self.g = Grafo(self.matriz1, True)
        self.assertEqual(self.g.mat_incid, self.resultado1)
    
    def test_matriz2(self):
        self.g = Grafo(self.matriz2, True)
        self.assertEqual(self.g.mat_incid, self.resultado2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
