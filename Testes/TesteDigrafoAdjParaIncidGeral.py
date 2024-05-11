from Classes.Digrafo import Digrafo
import unittest

class TesteDigrafoAdjParaIncidGeral(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.matriz1 = [
            [0, 1, 1],
            [-1, 0, 0],
            [-1, 0, 0]
        ]
        self.resultado1 = [
            [1, 1],
            [-1, 0],
            [0, -1]
        ]

        self.matriz2 = [
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0]
        ]
        self.resultado2 = [
            [0, 1, 0, 0],
            [0, -1, -1, 0],
            [0, 0, 1, -1],
            [0, 0, 0, 1]
        ]

        self.matriz3 = [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
        self.resultado3 = [
            [1, -1],
            [-1, 1],
            [0, 0]
        ]

        self.matriz4 = [
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 2],
            [0, 0, 2, 0]
        ]
        self.resultado4 = [
            [1, -1, 0, 0, 0, 0, 0, 0],
            [-1, 1, 1, -1, 0, 0, 0, 0],
            [0, 0, -1, 1, 1, 1, -1, -1],
            [0, 0, 0, 0, -1, -1, 1, 1]
        ]

        self.matriz5 = [
            [1, 0, 0],
            [1, 0, 0],
            [1, 2, 1]
        ]
        self.resultado5 = [
            [0, -1, 0, -1, 0, 0],
            [0, 1, 0, 0, -1, -1],
            [0, 0, 0, 1, 1, 1]
        ]

        self.matriz6 = [
            [0, 1, 0, 1],
            [0, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 1, 0]
        ]
        self.resultado6 = [
            [1, 1, 0, 0, 0],
            [-1, 0, 1, 1, 0],
            [0, 0, -1, 0, -1],
            [0, -1, 0, -1, 1]
        ]

        self.matriz7 = [
            [0, 1, 0, 1],
            [0, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0]
        ]
        self.resultado7 = [
            [1, 1, 0, 0, 0, 0],
            [-1, 0, 1, 1, -1, 0],
            [0, 0, -1, 0, 0, -1],
            [0, -1, 0, -1, 1, 1]
        ]

        self.matriz8 = [
            [0, 0, 0],
            [0, 1, 1],
            [2, 1, 0]
        ]

        self.resultado8 = [
            [0, 0, -1, -1, 0],
            [0, 1, 0, 0, -1],
            [0, -1, 1, 1, 1]
        ]
    
    def test_matriz1(self):
        self.dg = Digrafo(self.matriz1)
        self.assertEqual(self.dg.mat_incid, self.resultado1)
    
    def test_matriz2(self):
        self.dg = Digrafo(self.matriz2)
        self.assertEqual(self.dg.mat_incid, self.resultado2)
    
    def test_matriz3(self):
        self.dg = Digrafo(self.matriz3)
        self.assertEqual(self.dg.mat_incid, self.resultado3)
    
    def test_matriz4(self):
        self.dg = Digrafo(self.matriz4)
        self.assertEqual(self.dg.mat_incid, self.resultado4)
    
    def test_matriz5(self):
        self.dg = Digrafo(self.matriz5)
        self.assertEqual(self.dg.mat_incid, self.resultado5)
    
    def test_matriz6(self):
        self.dg = Digrafo(self.matriz6)
        self.assertEqual(self.dg.mat_incid, self.resultado6)
    
    def test_matriz7(self):
        self.dg = Digrafo(self.matriz7)
        self.assertEqual(self.dg.mat_incid, self.resultado7)
    
    def test_matriz8(self):
        self.dg = Digrafo(self.matriz8)
        self.assertEqual(self.dg.mat_incid, self.resultado8)


if __name__ == '__main__':
    unittest.main(verbosity=2)
