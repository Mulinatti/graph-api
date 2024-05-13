import unittest

# Uma matriz é uma lista de listas de inteiros
type Matriz = list[list[int]]

def contar_arestas(adjacencias: Matriz) -> int:
        num_arestas = 0
        for i in range(len(adjacencias)):
            for j in range(i, len(adjacencias)):
                if i <= j:
                    num_arestas += adjacencias[i][j]
        return num_arestas


class TestContarArestas(unittest.TestCase):
     def test_1(self):
          """Testar um grafo bem básico mesmo."""
          self.assertEqual(contar_arestas([
               [0, 1, 0, 0],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [0, 0, 1, 0]
          ]), 3)
     
     def test_2(self):
          """Testar um grafo não valorado com laço."""
          self.assertEqual(contar_arestas([
               [1, 1, 0],
               [1, 0, 1],
               [0, 1, 1]
          ]), 4)
     
     def test_3(self):
          """Testar um grafo com arestas múltiplas."""
          self.assertEqual(contar_arestas([
               [0, 2, 2],
               [2, 0, 2],
               [2, 2, 0]
          ]), 6)
     
     def test_4(self):
          """Testar um grafo valorado."""
          self.assertEqual(contar_arestas([
               [0, 20, 5],
               [20, 0, 15],
               [5, 15, 0]
          ]), 3)
     
     def test_5(self):
          """Testar um grafo valorado e com laço."""
          self.assertEqual(contar_arestas([
               [15, 3, 2],
               [3, 0, 0],
               [2, 0, 0]
          ]), 3)
     
     def test_6(self):
          """Testar um digrafo bem simples mesmo."""
          self.assertEqual(contar_arestas([
               [0, 1, 1],
               [0, 0, 0],
               [0, 0, 0]
          ]), 2)
     
     def test_7(self):
          """Testar um digrafo com laço."""
          self.assertEqual(contar_arestas([
               [1, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0]
          ]), 4)
     
     def test_8(self):
          """Testar um digrafo com aresta dupla."""
          self.assertEqual(contar_arestas([
               [0, 1, 0],
               [1, 0, 0],
               [0, 0, 0]
          ]), 2)
     
     def test_9(self):
          """Testar um digrafo com múltiplas arestas."""
          self.assertEqual(contar_arestas([
               [0, 1, 0, 0],
               [1, 0, 1, 0],
               [0, 1, 0, 2],
               [0, 0, 2, 0]
          ]), 8)
     
     def test_10(self):
          """Testar um digrafo com laço e arestas duplas."""
          self.assertEqual(contar_arestas([
               [0, 0, 0],
               [0, 1, 1],
               [2, 1, 0]
          ]), 5)
     
     def test_11(self):
         """Testar um digrafo valorado."""
         self.assertEqual(contar_arestas([
             [0, 5, 0],
             [0, 0, 10],
             [0, 0, 0]
         ], True, True), 2)

if __name__ == '__main__':
     unittest.main(verbosity=2)
