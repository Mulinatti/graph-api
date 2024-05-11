from Classes.Grafo import Grafo
import unittest

class TesteGrafoAdjParaIncidLaco(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.matriz1 = [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1]
        ]
        self.resultado1 = [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1]
        ]

    def test_matriz1(self):
        self.g = Grafo(self.matriz1, False)
        self.assertEqual(self.g.mat_incid, self.resultado1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
