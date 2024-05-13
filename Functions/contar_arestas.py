import unittest

def contar_arestas(adjacencias: list[list[int]]) -> int:
        num_arestas = 0
        for i in range(len(adjacencias)):
            for j in range(i, len(adjacencias)):
                if i <= j:
                    num_arestas += adjacencias[i][j]
        return num_arestas


class TestContarArestas(unittest.TestCase):
     def test_1(self):
          self.assertEqual(contar_arestas([
               [0, 1, 0, 0],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [0, 0, 1, 0]
          ]), 3)


if __name__ == '__main__':
     unittest.main(verbosity=2)
